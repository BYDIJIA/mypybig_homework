import Vue from 'vue'
import App from './App.vue'
import dataV from '@jiaminghi/data-view'
import axios from 'axios'  
import echarts from 'echarts'
  require('echarts-wordcloud')
  Vue.prototype.$echarts = echarts
Vue.prototype.axios = axios.create({
  timeout:20000,//延时
  baseURL:'http://127.0.0.1:8000',//后端基地址
});  
Vue.use(dataV)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
