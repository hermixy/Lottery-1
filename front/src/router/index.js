import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/views/hello/HelloWorld'
import Main from '@/views/Main'
import TrendingToday from '@/components/TrendingToday.vue'
import ForecastNumber from '@/components/ForecastNumber.vue'

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
          name: '数据统计',
          component: TrendingToday
        },
        {
          path: 'forecastNumber',
          name: '玩法选择',
          component: ForecastNumber
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
