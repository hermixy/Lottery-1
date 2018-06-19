<template>
  <Row :gutter="30">
    <Col :md="24" :lg="10">
        <Row>
            <Col :md="12" :lg="24">
                <Row type="flex" align="middle">
                    <Col span="18">
                        <Input v-model="value_number" placeholder="号码格式01 02 07 09 10" maxlength="20" size="large">
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
                <Input v-model="value_numbers" :disabled="disabled" type="textarea" :rows="20" :style="{marginTop:'20px'}"
                 placeholder="预测号码" readonly=true></Input>
            </Col>
            </Row>
    </Col>
    <Col :md="24" :lg="14">
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
import http from '../utils/http'

export default {
  data () {
    return {
      loading: false,
      value_number_select: 'm2',
      tableColumns: [
        {
          title: '期号',
          key: 'data_period'
        },
        {
          title: '开奖号码',
          key: 'data_award'
        },
        {
          title: '类型',
          key: 'data_type'
        }
      ]
      // tableData:
    }
  },
  computed: {
  },
  methods: {
    collapsedSider () {
      this.$refs.side1.toggleCollapse()
    },
    toLoading: async function () {
      this.loading = true
      let number = this.value_number
      let re = /^(\d{2}\s)+\d{2}$/
      if (!re.test(number)) {
        alert('Flase')
      } else {
        this.loading = true
        let params = {
          type: this.value_number_select,
          numbers: number.replace(/ /g, ',')
        }
        const res = await http.post('/lottery', params)
        if (http.isSuccess) {
          this.loading = false
          let listData = res.listData
          let content = ''
          let index = 0
          for (let i = 0; i < listData.length; i++) {
            if (index > 0) {
              content = content + '\n'
            }
            content = content + listData[i].number
            index++
          }
          this.value_numbers = content
          // this.disabled = true
        }
      }
      this.loading = false
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
