<template>
  <Table :style="{marginTop:'16px', marginBottom: '16px'}" :loading="tableLoading"
      stripe  border :columns="columns" :data="columnsData" height="444"></Table>
</template>
<script>
import http from '../utils/http'
export default {
  data () {
    return {
      columns: [
        {
          title: '期号',
          key: 'data_period'
        },
        {
          title: '开奖号码',
          key: 'data_award'
        }
      ],
      columnsData: [],
      tableLoading: true
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
    }
  }
}
</script>

<style scoped>
</style>
