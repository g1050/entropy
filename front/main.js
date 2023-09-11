import App from './App'

// #ifndef VUE3
import Vue from 'vue'
import './uni.promisify.adaptor'
import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:8000/entropy_decrease'; // 设置你的后端接口地址

// 将 axios 设置为 Vue 的原型属性，这样在组件中就可以通过 this.$axios 访问
Vue.prototype.$axios = axios;

Vue.config.productionTip = false
App.mpType = 'app'
const app = new Vue({
  ...App
})
app.$mount()
// #endif

// #ifdef VUE3

import { createSSRApp } from 'vue'
export function createApp() {
  const app = createSSRApp(App)
  return {
    app
  }
}
// #endif

