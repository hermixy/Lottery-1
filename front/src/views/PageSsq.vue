<template>
  <Table :style="{marginTop:'16px', marginBottom: '16px'}"
      stripe :columns="columns" :data="data"></Table>
</template>
<script>
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
      ]
    }
  }
}
</script>

<style scoped>
</style>
