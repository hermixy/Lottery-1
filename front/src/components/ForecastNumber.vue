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
            <Table border stripe :loading="tableLoading" height="452" :columns="tableColumns"
             :data="tableData" :class="getTableData"
             :row-class-name="tableRowClassName"></Table>
        </div>
    </Col>
  </Row>
</template>

<script>
import http from '../utils/http'
import util from '../utils/util'

export default {
  data () {
    return {
      loading: false,
      value_number_select: 'm2',
      tableLoading: true,
      tableColumns: [
        {
          title: '期号',
          key: 'data_period',
          align: 'center',
          sortable: true,
          sortType: 'desc'
        },
        {
          title: '开奖号码',
          align: 'center',
          key: 'data_award'
        },
        {
          title: '类型',
          align: 'center',
          key: 'data_type'
        }
      ],
      tableData: []
    }
  },
  computed: {

  },
  mounted: function () {
    this.getOpenData()
    setInterval(this.getOpenData, 60000)
  },
  methods: {
    toLoading: async function () {
      this.loading = true
      let number = this.value_number
      let re = /^(\d{2}\s)+\d{2}$/
      if (!re.test(number)) {
        this.$Message.warning('格式不正确，例如01 02 03 04 05')
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
    },
    getOpenData: async function () {
      let date = util.dataFormat(new Date(), 'yyyyMMdd')
      this.tableLoading = true
      let params = {
        date: date.substring(2)
      }
      const res = await http.post('/lottery/getOpenData', params)
      if (http.isSuccess) {
        let listData = res.listData
        const data = []
        for (let i = 0; i < listData.length; i++) {
          let type = listData[i].data_type
          if (type === 'M1') {
            data.push({
              data_period: listData[i].data_period,
              data_award: listData[i].data_award,
              data_type: type,
              cellClassName: {
                data_type: 'table-info-cell-type1'
              }
            })
          } else if (type === 'M2') {
            data.push({
              data_period: listData[i].data_period,
              data_award: listData[i].data_award,
              data_type: type,
              cellClassName: {
                data_type: 'table-info-cell-type2'
              }
            })
          } else if (type === 'M3') {
            data.push({
              data_period: listData[i].data_period,
              data_award: listData[i].data_award,
              data_type: type,
              cellClassName: {
                data_type: 'table-info-cell-type3'
              }
            })
          } else if (type === 'M4') {
            data.push({
              data_period: listData[i].data_period,
              data_award: listData[i].data_award,
              data_type: type,
              cellClassName: {
                data_type: 'table-info-cell-type4'
              }
            })
          } else {
            data.push({
              data_period: listData[i].data_period,
              data_award: listData[i].data_award,
              data_type: type
            })
          }
        }
        this.tableData = data
        this.tableLoading = false
      }
    }

    // tableRowClassName (row, index) {
    //   if (row.data_type === 'M1') {
    //     console.log(row.data_type + ' ' + index)
    //   }
    // }
  }
}
</script>

<style>
  .card-title {
    color: #abafbd;
    font-size: 20px;
  }
  .ivu-table .table-info-cell-type1 {
    color: rgb(243, 18, 18);
    font-weight: bold;
  }
  .ivu-table .table-info-cell-type2 {
    color: rgb(3, 160, 250);
    font-weight: bold;
  }
  .ivu-table .table-info-cell-type3 {
    color: rgb(239, 243, 4);
    font-weight: bold;
  }
  .ivu-table .table-info-cell-type4 {
    color: rgb(41, 228, 17);
    font-weight: bold;
  }
</style>
