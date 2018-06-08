<template>

    <ve-line :data="chartData"></ve-line>

</template>
<script>
export default {
  data () {
    return {
      chartData: {
        columns: ['类型', '今日', '昨日'],
        rows: [
          { '类型': 'M0', '今日': 13, '昨日': 93 },
          { '类型': 'M1', '今日': 35, '昨日': 32 },
          { '类型': 'M2', '今日': 23, '昨日': 26 },
          { '类型': 'M3', '今日': 72, '昨日': 14 },
          { '类型': 'M4', '今日': 37, '昨日': 49 }
        ]
      }
    }
  }
}
</script>
