import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/views/hello/HelloWorld'
import Main from '@/views/Main'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main,
      redirect: '/forecastNumber',
      children: [
        {
          path: 'trendingToday',
          name: 'trendingToday',
          component: resolve => require(['@/views/TrendingToday.vue'], resolve),
          meta: { title: '数据统计' }
        },
        {
          path: 'forecastNumber',
          name: '玩法选择',
          component: resolve => require(['@/views/ForecastNumber.vue'], resolve),
          meta: { title: '11选5辅助' }
        },
        {
          path: 'szc/:type',
          name: 'szc',
          component: resolve => require(['@/views/PageSzc.vue'], resolve),
          meta: { title: '数字彩' }
        }
      ]
    },
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
