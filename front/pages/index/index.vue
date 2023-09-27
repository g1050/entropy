<template>
	<view class="container">
		<uni-section title="Percentage" type="line">
		</uni-section>
		<view class="uni-padding-wrap uni-common-mt">
			<view style="margin-bottom: 10px;" class="demo-uni-col dark">
				<view class="progress-box">
					<progress :percent="Math.round((currentScore/targetScore)*100)" show-info stroke-width="3" />
				</view>
			</view>
		</view>
		<uni-section title="Base Info" type="line">
		</uni-section>
		<uni-card :is-shadow="false" is-full>
		<view class="input-row " style="margin-bottom: 10px;">
			<text>Current Score：{{ currentScore }}</text>
			<button class="mini-btn" type="" size="mini" @click="sendIncreaseRequest('reset')">Reset</button>
		</view>
		<view class="input-row" style="margin-bottom: 10px;">
			<text>Target Score：</text>
			<input type="number" v-model="targetScore" placeholder="请输入数字">
			<button class="mini-btn" type="" size="mini" @click="resetTargetScore">Reset</button>
		</view>
		<view class="input-row" style="margin-bottom: 10px;">
			<text>max random：</text>
			<input type="number" v-model="maxRandom" placeholder="请输入数字">
			<button class="mini-btn" type="" size="mini" @click="setRandom">Reset</button>
		</view>
		<view class="input-row" style="margin-bottom: 10px;">
			<text>min random：</text>
			<input type="number" v-model="minRandom" placeholder="请输入数字">
			<button class="mini-btn" type="" size="mini" @click="setRandom">Reset</button>
		</view>
		</uni-card>
		<uni-section title="Expect" type="line">
		</uni-section>
				<uni-card :is-shadow="false" is-full>
					<uni-row>
						<text class="uni-h6">Avarage random: ({{this.maxRandom}} + {{this.minRandom}})/2={{(this.maxRandom+this.minRandom)/2}}</text>
					</uni-row>
					<uni-row>
						<text class="uni-h6">Avarage time to achieve target: {{this.targetScore}} / {{(this.maxRandom+this.minRandom)/2}}={{Math.round(this.targetScore/((this.maxRandom+this.minRandom)/2))}}</text>
						
					</uni-row>
					
				</uni-card>
		<uni-section title="Action" type="line">
			<view class="example-body box">
				<button class="button popup-success"
					@click="messageToggle('success');sendIncreaseRequest('increase')"><text
						class="button-text success-text">Increase</text></button>
				<button class="button popup-error" @click="messageToggle('error');sendIncreaseRequest('decrease')"><text
						class="button-text error-text">Decrease</text></button>
			</view>
		</uni-section>


		<view>
			<!-- 提示信息弹窗 -->
			<uni-popup ref="message" type="message">
				<uni-popup-message :type="msgType" :message="messageText" :duration="2000"></uni-popup-message>
			</uni-popup>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				myurl:"https://79968ie682.imdo.co/",
				title: 'Hello',
				numberValue: null,
				currentScore: 0,
				targetScore: 0,
				maxRandom: 0,
				minRandom: 0,
				type: 'center',
				msgType: 'success',
				messageText: '这是一条成功提示',
				value: '',
				randomNum: 0,
			}
		},
		onReady() {},
		onLoad() {
			console.log("Hello")
			console.log(this.myurl);
			// 在页面加载时发送HTTP请求
			uni.request({
				url: this.myurl + '/entropy_decrease/score/',
				method: 'GET',
				data: {
					userid: 1
				},
				success: (res) => {
					// 处理成功响应
					if (res.statusCode === 200) {
						// 更新页面数据
						this.targetScore = res.data.target_score;
						this.currentScore = res.data.total_score;
						this.maxRandom = res.data.max;
						this.minRandom = res.data.min;
					} else {
						console.error('HTTP请求失败:', res);
					}
				},
				fail: (err) => {
					console.error('HTTP请求失败:', err);
				}
			});

		},
		methods: {
			messageToggle(type) {

			},
			sendIncreaseRequest(action) {
				// 构建请求URL
				const url = this.myurl + `/entropy_decrease/total_score/?userid=1&tag=${action}`;

				// 发送HTTP请求
				uni.request({
					url: url,
					method: 'PUT',
					success: (res) => {
						// 处理成功响应
						if (res.statusCode === 200) {
							// 根据需要处理响应数据
							console.log(`${action} request successful`, res.data);
							console.log(res.data.random_num)
							this.currentScore = res.data.total_score
							this.minRandom = res.data.min
							this.maxRandom = res.data.max
							this.randomNum = res.data.random_number
							var sig = ""
							if (action == "increase") {
								sig = "+"
								this.msgType = 'success'
							} else {
								sig = "-"
								this.msgType = 'error'
							}
							this.messageText = sig + this.randomNum + ""
							this.$refs.message.open()
						} else {
							console.error('HTTP请求失败:', res);
						}
					},
					fail: (err) => {
						console.error('HTTP请求失败:', err);
					}
				});
			},
			setRandom(action) {
				uni.request({
					url: this.myurl + `/entropy_decrease/range/?userid=1&min=${this.minRandom}&max=${this.maxRandom}`,
					method: 'POST',
					data: {}, // 如果需要发送请求体数据，在这里添加数据对象
					header: {
						'Content-Type': 'application/json', // 根据服务器要求设置合适的Content-Type
					},
					success: function(res) {
						console.log('请求成功', res.data);
						this.maxRandom = res.data.max;
						this.minRandom = res.minRandom;
					},
					fail: function(err) {
						console.error('请求失败', err);
						// 处理请求失败的情况
					}
				});

			},
			resetTargetScore(action) {
				// 构建请求URL
				const url =
					this.myurl + `/entropy_decrease/target_score/?userid=1&target_score=${this.targetScore}`;

				// 发送HTTP请求
				uni.request({
					url: url,
					method: 'PUT',
					success: (res) => {
						// 处理成功响应
						if (res.statusCode === 200) {
							// 根据需要处理响应数据
							console.log(`${action} request successful`, res.data);
							this.targetScore = res.data.target_score
						} else {
							console.error('HTTP请求失败:', res);
						}
					},
					fail: (err) => {
						console.error('HTTP请求失败:', err);
					}
				});
			},
		}
	}
</script>

<style>
	.demo-uni-col {
		height: 36px;
		border-radius: 10px;
	}

	.dark {
		background-color: #d3dce6;
	}

	.light {
		background-color: #e5e9f2;
	}

	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}

	.uni-padding-wrap {
		padding: 20rpx;
	}

	.input-row {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
	}

	.reset-target {
		display: flex;
		align-items: center;
	}

	.button-row {
		display: flex;
		align-items: center;
	}
</style>

<style lang="scss">
	@mixin flex {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
	}

	@mixin height {
		/* #ifndef APP-NVUE */
		height: 100%;
		/* #endif */
		/* #ifdef APP-NVUE */
		flex: 1;
		/* #endif */
	}

	.box {
		@include flex;
	}

	.button {
		@include flex;
		align-items: center;
		justify-content: center;
		flex: 1;
		height: 35px;
		margin: 0 5px;
		border-radius: 5px;
	}

	.example-body {
		background-color: #fff;
		padding: 10px 0;
	}

	.button-text {
		color: #fff;
		font-size: 12px;
	}

	.popup-content {
		@include flex;
		align-items: center;
		justify-content: center;
		padding: 15px;
		height: 50px;
		background-color: #fff;
	}

	.popup-height {
		@include height;
		width: 200px;
	}

	.text {
		font-size: 12px;
		color: #333;
	}

	.popup-success {
		color: #fff;
		background-color: #e1f3d8;
	}

	.popup-warn {
		color: #fff;
		background-color: #faecd8;
	}

	.popup-error {
		color: #fff;
		background-color: #fde2e2;
	}

	.popup-info {
		color: #fff;
		background-color: #f2f6fc;
	}

	.success-text {
		color: #09bb07;
	}

	.warn-text {
		color: #e6a23c;
	}

	.error-text {
		color: #f56c6c;
	}

	.info-text {
		color: #909399;
	}

	.dialog,
	.share {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: column;
	}

	.dialog-box {
		padding: 10px;
	}

	.dialog .button,
	.share .button {
		/* #ifndef APP-NVUE */
		width: 100%;
		/* #endif */
		margin: 0;
		margin-top: 10px;
		padding: 3px 0;
		flex: 1;
	}

	.dialog-text {
		font-size: 14px;
		color: #333;
	}
</style>