<style scoped>
    a {
        cursor:pointor;
    }
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }
    .layout-header-bar{
        background: #fff;
        box-shadow: 0 1px 1px rgba(0,0,0,.1);
        /* position: relative; */
    }
    .header-avator-con{
        position: absolute;
        right: 0;
        top: 0;
        height: 100%;
        padding-right: 14px;
    }
    .head-rules{
        position: absolute;
        right: 0;
        top: 0;
        height: 100%;
        padding-right: 14px;
    }

    .main-user-name{
        display: inline-block;
        width: 80px;
        word-break: keep-all;
        white-space: nowrap;
        vertical-align: middle;
        overflow: hidden;
        text-overflow: ellipsis;
        text-align: right;
    }
    .layout-logo-left{
        width: 90%;
        height: 30px;
        background: #5b6270;
        border-radius: 3px;
        margin: 15px auto;
    }
    .menu-icon{
        transition: all .3s;
    }
    .rotate-icon{
        transform: rotate(-90deg);
    }
    .menu-item span{
        display: inline-block;
        overflow: hidden;
        width: 69px;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: bottom;
        transition: width .2s ease .2s;
    }
    .menu-item i{
        transform: translateX(0px);
        transition: font-size .2s ease, transform .2s ease;
        vertical-align: middle;
        font-size: 16px;
    }
    .collapsed-menu span{
        width: 0px;
        transition: width .2s ease;
    }
    .collapsed-menu i{
        transform: translateX(5px);
        transition: font-size .2s ease .2s, transform .2s ease .2s;
        vertical-align: middle;
        font-size: 22px;
    }
    .layout-footer-center{
        text-align: center;
    }
    .support{
        position: absolute;
        right: 0;
        bottom: 0;
    }
</style>
<template>
    <div class="layout">
        <Layout >
            <Sider ref="side1" hide-trigger collapsible :collapsed-width="78" v-model="isCollapsed">
                <Menu active-name="1-1" theme="dark" width="auto" :open-names="['1']" accordion>
                    <Submenu name="1">
                        <template slot="title">
                            <Icon type="ios-analytics"></Icon>
                            11选5
                        </template>
                        <MenuItem name="1-1" @click.native="toGoForecastNumber">
                            <span>山东11选5</span>
                        </MenuItem>
                        <MenuItem name="10" @click.native="toGoForecastNumber">
                            <span>广东11选5</span>
                        </MenuItem>
                        <MenuItem name="11" @click.native="toGoForecastNumber">
                            <span>江西11选5</span>
                        </MenuItem>
                        <MenuItem name="12" @click.native="toGoForecastNumber">
                            <span>江苏11选5</span>
                        </MenuItem>
                        <MenuItem name="2" @click.native="toGoTrendingToday">
                            <Icon type="ios-navigate"></Icon>
                            <span>数据统计</span>
                        </MenuItem>
                    </Submenu>
                    <Submenu name="3">
                        <template slot="title">
                            <Icon type="ios-analytics"></Icon>
                            数字彩
                        </template>
                        <MenuItem name="3" @click.native="toGoSsq">
                            <Icon type="ios-navigate"></Icon>
                            <span>双色球</span>
                        </MenuItem>
                        <MenuItem name="4" @click.native="toGoForecastNumber">
                            <Icon type="ios-navigate"></Icon>
                            <span>大乐透</span>
                        </MenuItem>
                        <MenuItem name="5" @click.native="toGoForecastNumber">
                            <Icon type="ios-navigate"></Icon>
                            <span>七星彩</span>
                        </MenuItem>
                        <MenuItem name="6" @click.native="toGoForecastNumber">
                            <Icon type="ios-navigate"></Icon>
                            <span>七乐彩</span>
                        </MenuItem>
                        <MenuItem name="7" @click.native="toGoForecastNumber">
                            <Icon type="ios-navigate"></Icon>
                            <span>福彩3D</span>
                        </MenuItem>
                        <MenuItem name="8" @click.native="toGoForecastNumber">
                            <Icon type="ios-navigate"></Icon>
                            <span>排列三</span>
                        </MenuItem>
                        <MenuItem name="9" @click.native="toGoForecastNumber">
                            <Icon type="ios-navigate"></Icon>
                            <span>排列五</span>
                        </MenuItem>
                    </Submenu>
                </Menu>
                <!-- <p style="color: #F9453E; font-size: 14px; position:absolute; bottom:0; width:100%; height:80px;text-align: center;" >投注有风险，投资需谨慎</p> -->
                <Adsense
                    data-ad-client="ca-pub-8836920368192866"
                    data-ad-slot="8089222718">
                </Adsense>
            </Sider>
            <Layout>
                <Header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
                    <Icon @click.native="collapsedSider" :class="rotateIcon" type="md-menu" size="24"></Icon>
                    <!-- <div class="header-avator-con">
                        <Row type="flex" justify="end" align="middle" class="user-dropdown-innercon">
                            <Dropdown transfer trigger="click" @on-click="handleClickUserDropdown">
                                <a href="javascript:void(0)">
                                    <span class="main-user-name">{{ userName }}</span>
                                    <Icon type="arrow-down-b"></Icon>
                                </a>
                                <DropdownMenu slot="list">
                                     <DropdownItem name="ownSpace">个人中心</DropdownItem>
                                     <DropdownItem name="loginout">退出登录</DropdownItem>
                                </DropdownMenu>
                            </Dropdown>
                           <Avatar :style="{background: '#f56a00', marginLeft: '10px'}" size="large" icon="person">{{ userName }}</Avatar>
                        </Row>
                    </div> -->
                    <div class="head-rules">
                        <Row type="flex" justify="end" align="middle">
                            <a style="color: #3399ff; font-size: 16px; font-weight: bold;} " href="#" @click="rules_modal = true">玩法说明
                                <Icon type="help-circled"></Icon>
                            </a>
                            <Modal
                                v-model="rules_modal"
                                title="玩法说明"
                                @on-ok="ok"
                                @on-cancel="cancel">
                                <p>本网站是从11个号码中随机选5个号码进行组合得出所有结果，在购买网站上把选择出来的5个号码的所有组合进行购买，只要当期顺序摇出的5个开奖号码中包含所选号码，即为中奖。中奖概率会大大提升，购买网站是可以一次性粘贴所有的结果一次性购买的，中奖率极高。</p>
                                <p>M0: 是指跟上期开奖没有重号；</p>
                                <p>M1: 是指跟上期开奖有一个重号；</p>
                                <p>M2: 是指跟上期开奖有两个重号；</p>
                                <p>M3: 是指跟上期开奖有三个重号；</p>
                                <p>M4: 是指跟上期开奖有四个重号；</p>
                                <p>筛选功能：可以选择你猜的类型，筛除号码，定胆号码，筛除大小比，筛除奇偶比，这样可以根据自己的判断得出自认为更好的结果，这样可以获得更少的组数，中更多的MONEY；</p>
                                <p>数据统计：可以查看往日开出来的类型，大小比，奇偶比，助你更好的选择；</p>
                                <p>偷偷的在这里告诉你，在所选的组数只要有一组中奖，就是中奖，一旦中奖，本次投注不会亏损本金。</p>
                                <p style="color: #F9453E; font-size: 14px;} ">投注有风险，投资需谨慎</p>
                            </Modal>
                        </Row>
                    </div>
                </Header>
                <Content :style="{margin: '12px', padding: '0px 20px 20px',background: '#fff', minHeight: '260px'}">
                    <div>
                        <keep-alive>
                            <router-view></router-view>
                        </keep-alive>
                    </div>
                </Content>
                <Footer class="layout-footer-center">
                    <!-- <router-link to="http://www.miitbeian.gov.cn/state/outPortal/loginPortal.action">京ICP备18037389号</router-link> -->
                    <!-- <a href="http://www.miitbeian.gov.cn/state/outPortal/loginPortal.action" target="_blank">
                        京ICP备18037389号
                    </a> -->
                    <a>京ICP备18037389号</a>
                    <!-- <a href="#" @click="goMiitbeian">京ICP备18037389号</a> -->
                </Footer>
                <Affix :offset-bottom="100" class="support" >
                    <ButtonGroup vertical>
                        <Button icon="ios-chatbubbles" @click="goSupport"></Button>
                    </ButtonGroup>
                </Affix>
            </Layout>
        </Layout>
    </div>
</template>
<script>
export default {
  data () {
    return {
      isCollapsed: false,
      userName: '我就是我',
      rules_modal: false
    }
  },
  computed: {
    rotateIcon () {
      return [
        'menu-icon',
        this.isCollapsed ? 'rotate-icon' : ''
      ]
    },
    menuitemClasses () {
      return [
        'menu-item',
        this.isCollapsed ? 'collapsed-menu' : ''
      ]
    }
  },
  methods: {
    collapsedSider () {
      this.$refs.side1.toggleCollapse()
    },
    toGoForecastNumber () {
      this.$router.push({path: '/forecastNumber'})
    },
    toGoTrendingToday () {
      this.$router.push({path: '/trendingToday'})
    },
    toGoSsq () {
      this.$router.push({path: '/ssq'})
    },
    rulesClick () {
    },
    goMiitbeian () {
      window.open('http://www.miitbeian.gov.cn/state/outPortal/loginPortal.action')
    },
    goSupport () {
      window.open('http://wpa.qq.com/msgrd?v=3&uin=35899345&site=qq&menu=yes')
    }
  },
  mounted: {
    // render: (h) => {
    // return h('p', {
    //     style: {
    //     fontSize: '13px'
    //     }
    // }, [
    //     h('a', {
    //     attrs: {
    //         href: 'http://www.miitbeian.gov.cn/state/outPortal/loginPortal.action',
    //         target: '_blank'
    //     }
    //     }, '京ICP备18037389号')
    // ])
    // }
  }
}
</script>
