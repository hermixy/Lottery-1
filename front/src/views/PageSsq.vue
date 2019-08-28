<template>
<div>
  <Row :gutter="30">
    <Col :md="6" :lg="8" :style="{marginTop:'16px', marginBottom: '16px'}" type="flex" justify="center" align="middle">
      <Button type="primary" @click="jx(1)">随机一注</Button>
      <Button type="primary" @click="jx(3)">随机三注</Button>
      <Button type="primary" @click="jx(5)">随机五注</Button>
      <div>
        <Input v-model="value_numbers" type="textarea" :rows="17"
            placeholder="机选号码" :style="{width: '100%',marginTop:'16px'}">
        </Input>
      </div>
    </Col>
    <Col :md="18" :lg="16" :style="{marginTop:'16px', marginBottom: '16px'}">
      <Table :loading="tableLoading"
          stripe  border :columns="columns" :data="columnsData" height="444"></Table>
    </Col>
  </Row>
</div>
</template>
<script>
import http from '../utils/http'
export default {
  data () {
    return {
      columns: [
        {
          title: '期号',
          align: 'center',
          key: 'data_period'
        },
        {
          title: '开奖号码',
          align: 'center',
          key: 'data_award'
        }
      ],
      columnsData: [],
      tableLoading: true,
      value_numbers: ''
    }
  },
  mounted: function () {
    this.getOpenData()
  },
  methods: {
    getOpenData: async function () {
      let params = {
        type: 'ssq'
      }
      const res = await http.post('/lottery/getOpenDataOf', params)
      if (http.isSuccess) {
        let listData = res.listData
        this.columnsData = listData
        this.tableLoading = false
      }
    },
    jx: async function (num) {
      let params = {
        type: 'ssq',
        count: num
      }
      const res = await http.post('/lottery/jx', params)
      if (http.isSuccess) {
        let listData = res.listData
        // let content = ''
        // let index = 0
        // for (let i = 0; i < listData.length; i++) {
        //   if (index > 0) {
        //     content = content + '\n'
        //   }
        //   content = content + listData[i].number
        //   index++
        // }
        // this.value_numbers = content
        console.log(listData)
      }
    }
  }
}
</script>

<style scoped>
</style>
