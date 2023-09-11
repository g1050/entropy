<template>
	<div class="login-container">
		<h1>用户登录</h1>
		<form novalidate>
			<div class="form-group">
				<label for="username">用户名：</label>
				<input v-model="username" type="text" id="username" required>
			</div>
			<div class="form-group">
				<label for="password">密码：</label>
				<input v-model="password" type="password" id="password" required>
			</div>
			<button @click.prevent="login">登录</button>
		</form>
	</div>
</template>
<script>
	export default {
		data() {
			return {
				username: '',
				password: '',
			};
		},
		methods: {
			login() {
				console.log(this.username)
				// 构建登录请求的数据
				const data = {
					username: this.username,
					password: this.password,
				};

				// 发送POST请求到后端的登录接口
				this.$axios.post('/login/', data)
					.then(response => {
						// 处理成功响应，可以根据后端返回的数据进行进一步操作
						console.log('登录成功：', response.data);
						// 这里可以添加跳转到其他页面的逻辑等
					})
					.catch(error => {
						// 处理请求失败的情况
						console.error('登录失败：', error);
						// 这里可以添加显示错误信息的逻辑等
					});
			},
		},
	};
</script>

<style scoped>
	.login-container {
		text-align: center;
		margin-top: 20px;
	}

	.form-group {
		margin-bottom: 10px;
	}

	button {
		background-color: #007bff;
		color: white;
		padding: 10px 20px;
		border: none;
		cursor: pointer;
	}

	button:hover {
		background-color: #0056b3;
	}
</style>