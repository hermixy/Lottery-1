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
            <Sider ref="side1" hide-trigger collapsible :collapsed-width="78" v-model="isCollapsed">
                <Menu active-name="1-2" theme="dark" width="auto" :class="menuitemClasses">
                    <MenuItem name="1-1">
                        <Icon type="happy-outline"></Icon>
                        <span>预测号码</span>
                    </MenuItem>
                    <MenuItem name="1-2">
                        <Icon type="connection-bars"></Icon>
                        <span>今日趋势</span>
                    </MenuItem>
                </Menu>
            </Sider>
            <Layout>
                <Header :style="{padding: 0}" class="layout-header-bar">
                    <Icon @click.native="collapsedSider" :class="rotateIcon" :style="{margin: '20px 20px 0'}" type="navicon-round" size="24"></Icon>
                </Header>
                <Content :style="{margin: '20px 20px 20px 10px', padding: '20px 20px 0',background: '#fff', minHeight: '260px'}">
                    <Row :gutter="10">
                       <Col :md="24" :lg="12">
                            <Row>
                                <Col>
                                   <Row type="flex">
                                        <Col span="16">
                                            <Input v-model="value_number" placeholder="请输入开奖号" size="large">
                                                <Select v-model="value_number_select" slot="append" style="width: 70px">
                                                    <Option value="m0">M0</Option>
                                                    <Option value="m1">M1</Option>
                                                    <Option value="m2">M2</Option>
                                                    <Option value="m3">M3</Option>
                                                    <Option value="m4">M4</Option>
                                                </Select>
                                            </Input>
                                        </Col>
                                        <Col span="8">
                                            <Button type="primary" :loading="loading" @click="toLoading" :style="{width: '85px', margin:'5px'}">
                                                <span v-if="!loading">执行</span>
                                                <span v-else>加载中</span>
                                            </Button>
                                        </Col>
                                    </Row>
                                </Col>
                             </Row>
                        </Col>
                        <Col :md="24" :lg="12">
                           <Input v-model="value_numbers" type="textarea" :rows="20" :style="{width: '300px',margin:'0 20px'}" placeholder="预测号码"></Input>
                        </Col>
                    </Row>
                    <Input v-model="value_numbers" type="textarea" :rows="20" :style="{width: '300px',margin:'0 20px'}" placeholder="预测号码"></Input>
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
      loading: false,
      isCollapsed: false
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
    toLoading () {
      this.loading = true
    }

  }
}
</script>
