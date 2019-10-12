// The Vue build veirsion to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
// import VueRouter from 'vue-router'
import App from './App.vue'
import router from './router'
// import Routers from './src/router/index.js'
import ViewUI from 'view-design'
// import ElementUI from 'element-ui'
// import VCharts from 'v-charts'
import VeLine from 'v-charts/lib/line.common'
import VeHistogram from 'v-charts/lib/histogram.common'
import VePie from 'v-charts/lib/pie.common'
// import 'element-ui/lib/theme-chalk/index.css'
import 'view-design/dist/styles/iview.css'
import Ads from 'vue-google-adsense'
import VueClipboard from 'vue-clipboard2'
// import Brusher from 'brusher'
// import { Button, Table, Row, Col, Input, Select, Switch } from 'iview'
// Vue.component('Button', Button)
// Vue.component('Table', Table)

// Vue.use(Brusher)
Vue.use(VueClipboard)
Vue.use(require('vue-script2'))

Vue.use(Ads)
// Vue.use(Ads.InArticleAdsense)
// Vue.use(Ads.InFeedAdsense)

// Vue.use(VueRouter)
Vue.use(ViewUI)
// Vue.use(ElementUI)
Vue.component(VeLine.name, VeLine)
Vue.component(VeHistogram.name, VeHistogram)
Vue.component(VePie.name, VePie)

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  /* 路由发生变化修改页面title */
  ViewUI.LoadingBar.start()
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

router.afterEach((to) => {
  ViewUI.LoadingBar.finish()
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
