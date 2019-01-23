import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/', // 访问路径
      name: 'HelloHaoge', // 识别用的
      component: HelloWorld // 路由徐有的组件
    }
  ]
})
