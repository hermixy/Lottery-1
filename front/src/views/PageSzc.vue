<template>
<div>
  <Row :gutter="30">
    <Col :md="6" :lg="8" :style="{marginTop:'16px', marginBottom: '16px'}" type="flex" justify="center" align="middle">
      <Button type="primary" @click="jx('1')">随机一注</Button>
      <Button type="primary" @click="jx('3')">随机三注</Button>
      <Button type="primary" @click="jx('5')">随机五注</Button>
      <div>
        <Input v-model="value_numbers" type="textarea" :rows="10"
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
  watch: {
    '$route' (to, from) {
      this.getOpenData()
    }
  },
  mounted: function () {
    this.getOpenData()
  },
  methods: {
    getType: function () {
      return this.$route.params.type
    },
    getOpenData: async function () {
      let params = {
        type: this.getType()
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
        type: this.getType(),
        count: num
      }
      const res = await http.post('/lottery/jx', params)
      if (http.isSuccess) {
        let listData = res.listData
        let content = this.value_numbers
        for (let i = 0; i < listData.length; i++) {
          content = content + listData[i].number + '\n'
        }
        this.value_numbers = content
      }
    }
  }
}
</script>

<style scoped>
</style>
