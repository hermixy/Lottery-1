<template>
  <Row :gutter="30" :style="{marginTop: '20px'}">
    <Col :md="24" :lg="12">
      <Card>
        <p slot="title">
            <Icon type="ios-film-outline"></Icon>
            近10日出现次数
        </p>
        <ve-line
          :data="chartData"
          :extend="extend"
          :settings="chartSettings"
          :loading="loading"
          ref="chart1">
        </ve-line>
      </Card>
    </Col>

    <Col :md="24" :lg="12">
    </Col>
  </Row>

</template>
<script>
import http from '../utils/http'

export default {
  data () {
    this.extend = {
      'xAxis.0.axisLabel.rotate': 45,
      series: {
        label: {
          normal: {
            show: false
          }
        }
      }
    }
    this.chartSettings = {
      // xAxisType: 'time'
    }
    return {
      chartData: {
        columns: ['date', 'M0', 'M1', 'M2', 'M3', 'M4'],
        rows: []
      }
    }
  },
  watch: {
    // this.$refs[`chart1`].echarts.resize()
  },
  mounted: function () {
    this.get5DayData()
  },
  methods: {
    get5DayData: async function () {
      let params = {
      }
      const res = await http.post('/lottery/getTypeCount10Day', params)
      if (http.isSuccess) {
        let data = res.data
        this.chartData.rows = data
      }
    }
  }

}
</script>
