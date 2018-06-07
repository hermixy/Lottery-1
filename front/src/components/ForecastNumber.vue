<template>
  <Row :gutter="30">
    <Col :md="24" :lg="9">
        <Row>
            <Col :md="12" :lg="24">
                <Row type="flex" align="middle">
                    <Col span="18">
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
                    <Col span="6">
                        <Button type="primary" :loading="loading" @click="toLoading" :style="{width: '85px', margin:'5px'}">
                            <span v-if="!loading">执行</span>
                            <span v-else>加载中</span>
                        </Button>
                    </Col>
                </Row>
            </Col>
            <Col :md="12" :lg="24">
                <Input v-model="value_numbers" type="textarea" :rows="20" :style="{marginTop:'20px'}" placeholder="预测号码"></Input>
            </Col>
            </Row>
    </Col>
    <Col :md="24" :lg="15">
        <p class="card-title">
            <Icon type="android-list"></Icon>
            今日开奖列表
        </p>
        <div :style="{marginTop:'10px'}">
            <Table border stripe height="452" :columns="tableColumns" :data="tableData" ></Table>
        </div>
    </Col>
  </Row>
</template>

<script>
export default {
  data () {
    return {
      loading: false,
      tableColumns: [
        {
          title: '期号',
          key: 'issue'
        },
        {
          title: '开奖号码',
          key: 'lucky_number'
        },
        {
          title: '类型',
          key: 'type_number'
        }
      ],
      tableData: [
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        },
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        },
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        },
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        },
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        },
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        },
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        },
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        },
        {
          issue: '201811111',
          lucky_number: '0204060709',
          type_number: 'M2'
        }
      ]
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

<style>
  .card-title{
        color: #abafbd;
        font-size: 20px;
    }
</style>
