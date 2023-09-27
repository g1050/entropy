<template>
	<view class="content">
		<view class="todo-header">
			<!-- 状态栏左侧 -->
			<view class="todo-header_left">
				<text class="active-text">{{ text }}</text>
				<text>{{ listData.length }}条</text>
			</view>
			<!-- 状态栏右侧 -->
			<view class="todo-header_right" v-for="(item, index) in tabList" :key="index">
				<view class="todo-header_right-item" :class="{ 'active-tab': tabIndex == index }" @click="tabClick(item, index)">{{ item }}</view>
			</view>
		</view>
		<view class="todo-content" v-for="(item, index) in listData" :key="item.title">
			<view class="todo-list" :class="{ 'todo--finish': item.select }" @click="childItem(item, index)">
				<view class="todo-list_checkbox"><view class="checkbox"></view></view>
				<view class="todo-list_content">{{ item.title }}</view>
			</view>
		</view>
		<!-- 字体图标 -->
		<view class="create-todo" @click="creat"><text class="iconfont iconhao1" :class="{ 'create-todo-active': tetxShow }"></text></view>
		<!-- 输入框 -->
		<view class="create-content" v-if="activeInput" :class="{ 'create-show': tetxShow }">
			<view class="create-content-box">
				<view class="create-input"><input type="text" v-model="InputValue" placeholder="请输入你要创建的todo" /></view>
				<view class="creat-button" @click="submitInput">创建</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			InputValue: '',
			activeInput: false,
			tabIndex: 0,
			tetxShow: false,
			text: '全部',
			tabList: ['全部', '待办', '已完成'],
			list: [{ title: '112326547889', select: false }, { title: 'aasdasdasd', select: true }]
		};
	},
	onLoad() {},
	computed: {
		listData() {
			let list = JSON.parse(JSON.stringify(this.list)); //拷贝对象
			let newList = [];
			//点击全部
			if (this.tabIndex == 0) {
				return list;
			}
			//点击待办
			if (this.tabIndex == 1) {
				list.forEach(v => {
					if (!v.select) {
						newList.push(v);
					}
				});
				return newList;
			}
			//点击已完成
			if (this.tabIndex == 2) {
				list.forEach(v => {
					if (v.select) {
						newList.push(v);
					}
				});
				return newList;
			}
		}
	},
	methods: {
		//切换tab
		tabClick(item, index) {
			this.text = item;
			this.tabIndex = index;
		},
		//点击项目
		childItem(item, index) {
			this.list[index].select = !this.list[index].select;
		},
		//打开输入框
		creat() {
			if (this.activeInput) {
				this.close();
			} else {
				this.open();
			}
		},
		//打开动画
		open() {
			this.activeInput = true;
			this.$nextTick(() => {
				setTimeout(() => {
					this.tetxShow = true;
				}, 50);
			});
		},
		//关闭动画
		close() {
			this.tetxShow = false;
			this.$nextTick(() => {
				setTimeout(() => {
					this.activeInput = false;
				}, 350);
			});
		},
		//点击创建
		submitInput() {
			if (this.InputValue == '') {
				uni.showToast({
					title: '输入的内容不能为空',
					icon: 'none'
				});
			} else {
				this.activeInput = false;
				this.list.unshift({
					title: this.InputValue,
					select: false
				});
				this.InputValue = '';
				this.close();
			}
		}
	}
};
</script>

<style>
/* @import '../../common/icon.css'; */
.todo-header {
	display: flex;
	align-items: center;
	padding: 0 15px;
	font-size: 12px;
	color: #333333;
	height: 45px;
	box-shadow: -1px 1px 5px 0 rgba(0, 0, 0, 0.1);
	background-color: #ffffff;
}
.todo-header_left {
	width: 100%;
}
.active-text {
	font-size: 14px;
	color: #279abf;
	padding-right: 10px;
}
.todo-header_right {
	display: flex;
	flex-shrink: 0;
}
.todo-header_right-item {
	padding: 0 5px;
}
.active-tab {
	color: #279abf;
}
.todo-content {
	position: relative;
}
.todo-list {
	position: relative;
	display: flex;
	align-items: center;
	padding: 15px;
	margin: 15px;
	color: #0c3854;
	font-size: 14px;
	border-radius: 10px;
	background: #cfebfd;
	box-shadow: -1px 1px 5px 1px rgba(0, 0, 0, 0.1), -1px 2px 1px 0 rgba(255, 255, 255) inset;
	overflow: hidden;
}
.todo-list::after {
	position: absolute;
	content: '';
	top: 0;
	bottom: 0;
	left: 0;
	width: 5px;
	background: #91d1e8;
}
.todo-list_checkbox {
	padding-right: 15px;
}
.checkbox {
	width: 20px;
	height: 20px;
	border-radius: 50%;
	background: #ffffff;
	box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.1);
}
.todo--finish .checkbox {
	position: relative;
	background: #eee;
}
.todo--finish .checkbox::after {
	content: '';
	position: absolute;
	width: 10px;
	height: 10px;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	border-radius: 50%;
	margin: auto;
	background: #cfebfd;
	box-shadow: 0 0 2px 0px rgba(0, 0, 0, 0.2) inset;
}
.todo--finish .todo-list_content {
	color: #999;
}
.todo--finish.todo-list:before {
	content: '';
	position: absolute;
	top: 0;
	bottom: 0;
	left: 40px;
	right: 10px;
	height: 2px;
	margin: auto 0;
	background: #bdcdd8;
}
.todo--finish.todo-list:after {
	background: #ccc;
}
.create-todo {
	display: flex;
	align-items: center;
	justify-content: center;
	position: fixed;
	bottom: 20px;
	left: 0;
	right: 0;
	margin: 0 auto;
	width: 50px;
	height: 50px;
	border-radius: 50%;
	background-color: #deeff5;
	box-shadow: -1px 1px 5px 2px rgba(0, 0, 0, 0.1), -1px 1px 1px 0 rgba(255, 255, 255) inset;
}
.iconhao1 {
	font-size: 30px;
	color: #add8e6;
}
.create-content {
	position: fixed;
	bottom: 95px;
	left: 20px;
	right: 20px;
	transition: all 0.3s;
	opacity: 0;
	transform: scale(0) translateY(200%);
}
.create-show {
	opacity: 1;
	transform: scale(1) translateY(0);
}
.create-content-box {
	display: flex;
	align-items: center;
	padding: 0 15px;
	padding-right: 0;
	border-radius: 50px;
	background: #deeff5;
	box-shadow: -1px 1px 5px 2px rgba(0, 0, 0, 0.1), -1px 1px 1px 0 rgba(255, 255, 255) inset;
	z-index: 2;
}
.create-input {
	width: 100%;
	padding-right: 15px;
	color: #add8e6;
}
.creat-button {
	display: flex;
	align-items: center;
	justify-content: center;
	flex-shrink: 0;
	height: 50px;
	width: 80px;
	border-radius: 50px;
	font-size: 16px;
	color: #88d4ec;
	box-shadow: -2px 0px 2px 1px rgba(0, 0, 0, 0.1);
}
.create-content:after {
	content: '';
	position: absolute;
	right: 0;
	left: 0;
	bottom: -8px;
	width: 20px;
	height: 20px;
	background: #deeff5;
	transform: rotate(45deg);
	margin: 0 auto;
	box-shadow: 1px 1px 5px 2px rgba(0, 0, 0, 0.1);
	z-index: -1;
}
.create-content-box:after {
	content: '';
	position: absolute;
	right: 0;
	left: 0;
	bottom: -8px;
	width: 20px;
	height: 20px;
	background: #deeff5;
	transform: rotate(45deg);
	margin: 0 auto;
}
.iconhao1 {
	transition: transform 0.3s;
}
.create-todo-active {
	transform: rotate(135deg);
}
</style>

