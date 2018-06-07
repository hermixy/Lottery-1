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
      children: [
        {
          path: 'trendingToday',
          name: '今日趋势',
          component: () => import('@/components/TrendingToday.vue')
        },
        {
          path: 'forecastNumber',
          name: '预测号码',
          component: () => import('@/components/ForecastNumber.vue')
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
