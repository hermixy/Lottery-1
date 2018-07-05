// The Vue build veirsion to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// import VueRouter from 'vue-router'
import App from './App.vue'
import router from './router'
// import Routers from './src/router/index.js'
import iView from 'iview'
// import ElementUI from 'element-ui'
// import VCharts from 'v-charts'
import VeLine from 'v-charts/lib/line.common'
// import 'element-ui/lib/theme-chalk/index.css'
import 'iview/dist/styles/iview.css'
import Ads from 'vue-google-adsense'

Vue.use(require('vue-script2'))

Vue.use(Ads.Adsense)
// Vue.use(Ads.InArticleAdsense)
// Vue.use(Ads.InFeedAdsense)

// Vue.use(VueRouter)
Vue.use(iView)
// Vue.use(ElementUI)
Vue.component(VeLine.name, VeLine)

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

// The routing configuration
// const RouterConfig = {
//   routes: Routers
// }

// const router = new VueRouter(RouterConfig)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  router: router,
  render: h => h(App)
})
