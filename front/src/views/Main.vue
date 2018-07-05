<style scoped>
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
        position: relative;
    }
    .header-avator-con{
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
</style>
<template>
    <div class="layout">
        <Layout :style="{minHeight: '100vh'}">
            <Sider ref="side1" breakpoint="sm" hide-trigger collapsible :collapsed-width="78" v-model="isCollapsed">
                <Menu active-name="1" theme="dark" width="auto" :class="menuitemClasses">
                    <MenuItem name="1" @click.native="toGoForecastNumber">
                        <Icon type="happy-outline"></Icon>
                        <span>山东11选5</span>
                    </MenuItem>
                    <MenuItem name="2" @click.native="toGoTrendingToday">
                        <Icon type="connection-bars"></Icon>
                        <span>数据统计</span>
                    </MenuItem>
                </Menu>
                <Adsense
                    data-ad-client="ca-pub-8836920368192866"
                    data-ad-slot="8089222718">
                </Adsense>
            </Sider>
            <Layout>
                <Header :style="{padding: 0}" class="layout-header-bar">
                    <Icon @click.native="collapsedSider" :class="rotateIcon" :style="{margin: '20px 20px 0'}" type="navicon-round" size="24"></Icon>
                    <div class="header-avator-con">
                        <Row type="flex" justify="end" align="middle" class="user-dropdown-innercon">
                            <Dropdown transfer trigger="click" @on-click="handleClickUserDropdown">
                                <a href="javascript:void(0)">
                                    <span class="main-user-name">{{ userName }}</span>
                                    <Icon type="arrow-down-b"></Icon>
                                </a>
                                <DropdownMenu slot="list">
                                    <!-- <DropdownItem name="ownSpace">个人中心</DropdownItem> -->
                                    <DropdownItem name="loginout">退出登录</DropdownItem>
                                </DropdownMenu>
                            </Dropdown>
                           <Avatar :style="{background: '#f56a00', marginLeft: '10px'}" size="large" icon="person">{{ userName }}</Avatar>
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
                <Footer class="layout-footer-center"> copyright©2017-2018</Footer>
            </Layout>
        </Layout>
    </div>
</template>
<script>
export default {
  data () {
    return {
      isCollapsed: false,
      userName: '我就是我'
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
    }
  }
}
</script>
