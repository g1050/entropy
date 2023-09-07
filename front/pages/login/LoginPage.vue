<template>
  <div class="login-container">
    <h1>用户登录</h1>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">用户名：</label>
        <input v-model="username" type="text" id="username" required>
      </div>
      <div class="form-group">
        <label for="password">密码：</label>
        <input v-model="password" type="password" id="password" required>
      </div>
      <button type="submit">登录</button>
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
      // 在这里编写登录逻辑，可以使用Ajax请求与后端服务器通信
      // 例如，你可以在这里发送POST请求来验证用户名和密码
      console.log('用户名：', this.username);
      console.log('密码：', this.password);
      // 这里可以添加实际的登录逻辑
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
