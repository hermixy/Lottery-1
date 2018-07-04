<template>
  <Row :gutter="30" :style="{marginTop: '20px'}">
    <Col :md="24" :lg="12">
      <Card>
        <p slot="title">
            <Icon type="ios-film-outline"></Icon>
            近五日出现次数
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
export default {
  data () {
    this.extend = {
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
        columns: ['类型', 'M0', 'M1', 'M2', 'M3', 'M4'],
        rows: [
          { '类型': '昨日', 'M0': 45, 'M1': 44, 'M2': 38, 'M3': 23, 'M4': 28 },
          { '类型': '0619', 'M0': 33, 'M1': 3, 'M2': 27, 'M3': 45, 'M4': 10 },
          { '类型': '0618', 'M0': 25, 'M1': 44, 'M2': 28, 'M3': 43, 'M4': 38 },
          { '类型': '0617', 'M0': 13, 'M1': 23, 'M2': 32, 'M3': 14, 'M4': 49 },
          { '类型': '0616', 'M0': 45, 'M1': 44, 'M2': 38, 'M3': 23, 'M4': 18 },
          { '类型': '0615', 'M0': 33, 'M1': 3, 'M2': 27, 'M3': 35, 'M4': 10 }
          // { '类型': '0614', 'M0': 25, 'M1': 54, 'M2': 28, 'M3': 43, 'M4': 38 },
          // { '类型': '0613', 'M0': 13, 'M1': 23, 'M2': 32, 'M3': 14, 'M4': 39 }
        ]
      }
    }
  },
  watch: {
    // this.$refs[`chart1`].echarts.resize()
  },
  mounted: function () {
  },
  methods: {
  }

}
</script>
