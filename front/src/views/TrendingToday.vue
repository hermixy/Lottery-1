<template>
<div>
  <BackTop></BackTop>
  <Row :gutter="20" :style="{marginTop: '20px'}">
    <Col :md="24" :lg="24">
      <Card id="card">
        <p slot="title">
            <Icon type="ios-film-outline"></Icon>
            近15日出现次数
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
  </Row>
  <Row :gutter="20">
    <Col :sm="24" :md="11" :lg="9" :style="{marginTop: '20px'}">
      <Card>
        <p slot="title">
            <Icon type="pie-graph"></Icon>
            昨日大小比出现次数
        </p>
        <ve-pie :data="chartData_daxiaobi_zuori" ref="chartData_daxiaobi_zuori_ref"></ve-pie>
      </Card>
    </Col>
    <Col :sm="24" :md="13" :lg="15" :style="{marginTop: '20px'}">
     <Card>
         <p slot="title">
            <Icon type="stats-bars"></Icon>
            近5日大小比出现次数
        </p>
        <ve-histogram :data="chartData_daxiaobi_5ri" ref="chartData_daxiaobi_5ri_ref"></ve-histogram>
      </Card>
    </Col>
  </Row>
  <Row :gutter="20">
    <Col :sm="24" :md="11" :lg="9" :style="{marginTop: '20px'}">
      <Card>
        <p slot="title">
            <Icon type="pie-graph"></Icon>
            昨日奇偶比出现次数
        </p>
        <ve-pie :data="chartData_qioubi_zuori" ref="chartData_qioubi_zuori_ref"></ve-pie>
      </Card>
    </Col>
    <Col :sm="24" :md="13" :lg="15" :style="{marginTop: '20px'}">
     <Card>
         <p slot="title">
            <Icon type="stats-bars"></Icon>
            近5日奇偶比出现次数
        </p>
        <ve-histogram :data="chartData_qioubi_5ri" ref="chartData_qioubi_5ri_ref"></ve-histogram>
      </Card>
    </Col>
  </Row>
</div>
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
            show: true
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
      },
      chartData_daxiaobi_zuori: {
        columns: ['item', 'num'],
        rows: []
      },
      chartData_daxiaobi_5ri: {
        columns: ['date', '0:5', '1:4', '2:3', '3:2', '4:1', '5:0'],
        rows: []
      },
      chartData_qioubi_zuori: {
        columns: ['item', 'num'],
        rows: []
      },
      chartData_qioubi_5ri: {
        columns: ['date', '0:5', '1:4', '2:3', '3:2', '4:1', '5:0'],
        rows: []
      }
    }
  },
  watch: function () {
    this.$nextTick(() => {
      this.$refs.chart1.echarts.resize()
      this.$refs.chartData_daxiaobi_zuori_ref.echarts.resize()
      this.$refs.chartData_daxiaobi_5ri_ref.echarts.resize()
      this.$refs.chartData_qioubi_zuori_ref.echarts.resize()
      this.$refs.chartData_qioubi_5ri_ref.echarts.resize()
    })
  },
  created: function () {
    this.$nextTick(() => {
      this.$refs.chart1.echarts.resize()
      this.$refs.chartData_daxiaobi_zuori_ref.echarts.resize()
      this.$refs.chartData_daxiaobi_5ri_ref.echarts.resize()
      this.$refs.chartData_qioubi_zuori_ref.echarts.resize()
      this.$refs.chartData_qioubi_5ri_ref.echarts.resize()
    })
  },
  mounted: function () {
    this.getDayData()
    this.getDxbDayData()
    this.getQobDayData()
  },
  methods: {
    getDayData: async function () {
      let params = {
        day: 15
      }
      const res = await http.post('/lottery/getTypeCountDay', params)
      if (http.isSuccess) {
        let data = res.data
        this.chartData.rows = data
      }
    },
    getDxbDayData: async function () {
      let params = {
      }
      const res = await http.post('/lottery/getDxbCountDay', params)
      if (http.isSuccess) {
        let data = res.data
        const dataAll = []
        const dataZuori = []
        for (let i = 0; i < data.length; i++) {
          dataAll.push({
            'date': data[i].date,
            '0:5': data[i].item05,
            '1:4': data[i].item14,
            '2:3': data[i].item23,
            '3:2': data[i].item32,
            '4:1': data[i].item41,
            '5:0': data[i].item50
          })
        }
        if (data != null && data.length > 0) {
          dataZuori.push({
            'item': '0:5',
            'num': data[0].item05
          })
          dataZuori.push({
            'item': '1:4',
            'num': data[0].item14
          })
          dataZuori.push({
            'item': '2:3',
            'num': data[0].item23
          })
          dataZuori.push({
            'item': '3:2',
            'num': data[0].item32
          })
          dataZuori.push({
            'item': '4:1',
            'num': data[0].item41
          })
          dataZuori.push({
            'item': '5:0',
            'num': data[0].item50
          })
        }
        this.chartData_daxiaobi_5ri.rows = dataAll
        this.chartData_daxiaobi_zuori.rows = dataZuori
        console.log(dataAll)
      }
    },
    getQobDayData: async function () {
      let params = {
      }
      const res = await http.post('/lottery/getQobCountDay', params)
      if (http.isSuccess) {
        let data = res.data
        const dataAll = []
        const dataZuori = []
        for (let i = 0; i < data.length; i++) {
          dataAll.push({
            'date': data[i].date,
            '0:5': data[i].item05,
            '1:4': data[i].item14,
            '2:3': data[i].item23,
            '3:2': data[i].item32,
            '4:1': data[i].item41,
            '5:0': data[i].item50
          })
        }
        if (data != null && data.length > 0) {
          dataZuori.push({
            'item': '0:5',
            'num': data[0].item05
          })
          dataZuori.push({
            'item': '1:4',
            'num': data[0].item14
          })
          dataZuori.push({
            'item': '2:3',
            'num': data[0].item23
          })
          dataZuori.push({
            'item': '3:2',
            'num': data[0].item32
          })
          dataZuori.push({
            'item': '4:1',
            'num': data[0].item41
          })
          dataZuori.push({
            'item': '5:0',
            'num': data[0].item50
          })
        }
        this.chartData_qioubi_5ri.rows = dataAll
        this.chartData_qioubi_zuori.rows = dataZuori
      }
    }
  }

}
</script>
