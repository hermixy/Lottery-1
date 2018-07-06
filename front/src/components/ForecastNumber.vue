<template>
<div>
  <Row :gutter="30" type="flex" align="middle">
    <Col :md="24" :lg="9" :style="{marginTop: '20px'}">
        <Row type="flex" align="middle">
            <Col span="18">
                <Input v-model="value_number" placeholder="号码格式01 02 03 04 05" :maxlength="20" size="large">
                    <Select v-model="value_number_select" slot="append" :disabled="value_number_select_disabled" style="width: 66px">
                        <Option value="m0">M0</Option>
                        <Option value="m1">M1</Option>
                        <Option value="m2">M2</Option>
                        <Option value="m3">M3</Option>
                        <Option value="m4">M4</Option>
                    </Select>
                </Input>
            </Col>
            <Col span="6">
                <Button type="primary" :loading="loading" @click="toLoading" :style="{width: '80px', margin:'5px'}">
                    <span v-if="!loading">执行</span>
                    <span v-else>加载中</span>
                </Button>
            </Col>
        </Row>
    </Col>
    <Col :md="24" :lg="15" :style="{marginTop: '20px'}">
        <Row type="flex" align="middle" :gutter="10">
          <Col>
            <i-switch v-model="sxSwitch" @on-change="sxSwichChange">
              <span slot="open">开</span>
              <span slot="close">关</span>
            </i-switch>
          </Col>
          <Col>
            <Button :disabled="sxBtnDisable"  @click="sxDialogClick">筛选</Button>
            <Modal
                v-model="sxDialog"
                title="筛选条件"
                :styles="{top: '20px'}"
                width="600"
                @on-ok="ok"
                @on-cancel="cancel">
                <p style="font-weight: bold">类型:</p>
                <Card :style="{marginTop:'10px'}">
                  <CheckboxGroup v-model="sx_type" size="large" @on-change="sxTypeChange">
                      <Checkbox label="m0">
                          <span>M0</span>
                      </Checkbox>
                      <Checkbox label="m1">
                          <span>M1</span>
                      </Checkbox>
                      <Checkbox label="m2">
                          <span>M2</span>
                      </Checkbox>
                      <Checkbox label="m3">
                          <span>M3</span>
                      </Checkbox>
                      <Checkbox label="m4">
                          <span>M4</span>
                      </Checkbox>
                  </CheckboxGroup>
                </Card>
                <br>
                <p style="font-weight: bold">筛除号码:</p>
                <Card :style="{marginTop:'10px'}">
                  <CheckboxGroup v-model="sx_sc" size="large" @on-change="sxShaiChuChange">
                      <Checkbox label="01"></Checkbox>
                      <Checkbox label="02"></Checkbox>
                      <Checkbox label="03"></Checkbox>
                      <Checkbox label="04"></Checkbox>
                      <Checkbox label="05"></Checkbox>
                      <Checkbox label="06"></Checkbox>
                      <Checkbox label="07"></Checkbox>
                      <Checkbox label="08"></Checkbox>
                      <Checkbox label="09"></Checkbox>
                      <Checkbox label="10"></Checkbox>
                      <Checkbox label="11"></Checkbox>
                  </CheckboxGroup>
                </Card>
                <br>
                <p style="font-weight: bold">定胆号码:</p>
                <Card :style="{marginTop:'10px'}">
                  <CheckboxGroup v-model="sx_dd" size="large" @on-change="sxDingDanChange">
                      <Checkbox label="01"></Checkbox>
                      <Checkbox label="02"></Checkbox>
                      <Checkbox label="03"></Checkbox>
                      <Checkbox label="04"></Checkbox>
                      <Checkbox label="05"></Checkbox>
                      <Checkbox label="06"></Checkbox>
                      <Checkbox label="07"></Checkbox>
                      <Checkbox label="08"></Checkbox>
                      <Checkbox label="09"></Checkbox>
                      <Checkbox label="10"></Checkbox>
                      <Checkbox label="11"></Checkbox>
                  </CheckboxGroup>
                </Card>
                <br>
                <p style="font-weight: bold">筛除大小比:</p>
                <Card :style="{marginTop:'10px'}">
                  <CheckboxGroup v-model="sx_dxb" size="large" @on-change="sxDaXiaoBiChange">
                      <Checkbox label="0:5">
                        <span>0 : 5</span>
                      </Checkbox>
                      <Checkbox label="1:4">
                        <span>1 : 4</span>
                      </Checkbox>
                      <Checkbox label="2:3">
                        <span>2 : 3</span>
                      </Checkbox>
                      <Checkbox label="3:2">
                        <span>3 : 2</span>
                      </Checkbox>
                      <Checkbox label="4:1">
                        <span>4 : 1</span>
                      </Checkbox>
                      <Checkbox label="5:0">
                        <span>5 : 0</span>
                      </Checkbox>
                  </CheckboxGroup>
                </Card>
                <br>
                <p style="font-weight: bold">筛除奇偶比:</p>
                <Card :style="{marginTop:'10px'}">
                  <CheckboxGroup v-model="sx_qob" size="large" @on-change="sxQiOuBiChange">
                      <Checkbox label="0:5">
                        <span>0 : 5</span>
                      </Checkbox>
                      <Checkbox label="1:4">
                        <span>1 : 4</span>
                      </Checkbox>
                      <Checkbox label="2:3">
                        <span>2 : 3</span>
                      </Checkbox>
                      <Checkbox label="3:2">
                        <span>3 : 2</span>
                      </Checkbox>
                      <Checkbox label="4:1">
                        <span>4 : 1</span>
                      </Checkbox>
                      <Checkbox label="5:0">
                        <span>5 : 0</span>
                      </Checkbox>
                  </CheckboxGroup>
                </Card>
                <br>
            </Modal>
          </Col>
        </Row>
    </Col>
  </Row>
  <Row :gutter="30">
    <Col :md="8" :lg="9" :style="{marginTop:'20px'}">
        <Card :style="{padding: '0px, 0px'}">
            <p slot="title">组选号码</p>
            <a href="#" slot="extra" @click="doCopy">
                <Icon type="clipboard"></Icon>
                复制
            </a>
            <Input v-model="value_numbers" type="textarea" :rows="17"
            placeholder="预测号码" :readonly="true" :style="{width: '100%'}"></Input>
            </br>
            <p :style="{marginTop:'10px', textAlign: 'center'}">共{{zhuNum}}组</p>
          </Card>
    </Col>
    <Col :md="16" :lg="15" >
        <Row :style="{marginTop:'16px'}" type="flex" align="middle">
          <Col>
            <p class="card-title" >
              <Icon type="android-list"></Icon>
              今日开奖列表
            </p>
          </Col>
          <Col>
            <p style="text-align: right; color: #abafbd;}">*自动会刷新</p>
          </Col>
        </Row>
        <div :style="{marginTop:'10px'}">
            <Table border stripe :loading="tableLoading" height="444" :columns="tableColumns"
            :data="tableData"></Table>
        </div>
    </Col>
  </Row>
</div>
</template>

<script>
import http from '../utils/http'
import util from '../utils/util'

export default {
  data () {
    return {
      loading: false,
      value_number: '',
      value_numbers: '',
      value_number_select: 'm2',
      value_number_select_disabled: false,
      sxDialog: false,
      sx_type: [],
      sx_sc: [],
      sx_dd: [],
      sx_dxb: [],
      sx_qob: [],
      tableLoading: true,
      sxSwitch: false,
      sxBtnDisable: true,
      zhuNum: '0',
      tableColumns: [
        {
          title: '期号',
          key: 'data_period',
          align: 'center',
          sortable: true,
          sortType: 'desc',
          fixed: 'left',
          width: 100
        },
        {
          title: '开奖号码',
          align: 'center',
          key: 'data_award',
          width: 160
        },
        {
          title: '类型',
          align: 'center',
          key: 'data_type',
          width: 100
        },
        {
          title: '大小比',
          align: 'center',
          key: 'data_size',
          width: 100
        },
        {
          title: '奇偶比',
          align: 'center',
          key: 'data_qiou',
          width: 100
        },
        {
          title: '质合比',
          align: 'center',
          key: 'data_zhihe',
          width: 100
        }
      ],
      tableData: []
    }
  },
  computed: {

  },
  mounted: function () {
    this.getOpenData()
    setInterval(this.getOpenData, 30000)
  },
  methods: {
    sxSwichChange (status) {
      this.sxBtnDisable = !status
      this.value_number_select_disabled = status
    },
    sxDialogClick () {
      this.sxDialog = true
    },
    sxTypeChange (data) {
      this.sx_type = data
    },
    sxShaiChuChange (data) {
      this.sx_sc = data
    },
    sxDingDanChange (data) {
      this.sx_dd = data
    },
    sxDaXiaoBiChange (data) {
      this.sx_dxb = data
    },
    sxQiOuBiChange (data) {
      this.sx_qob = data
    },
    ok () {
      if (this.sx_type) {
        this.value_number_select_disabled = true
      }
    },
    cancel () {
      this.$Message.info('您的筛选操作取消啦')
      this.sxBtnDisable = true
      this.sxSwitch = false
      this.sx_type = []
      this.sx_sc = []
      this.sx_dd = []
      this.sx_dxb = []
      this.sx_qob = []
      this.value_number_select_disabled = false
    },
    toLoading: async function () {
      this.loading = true
      let number = this.value_number
      let re = /^(\d{2}\s)+\d{2}$/
      if (!re.test(number)) {
        this.$Message.warning('格式不正确，例如01 02 03 04 05')
      } else {
        this.loading = true
        let sxType
        if (this.value_number_select_disabled === false) {
          sxType = this.value_number_select
        } else {
          if (this.sx_type.length === 0) {
            this.$Message.warning('筛选已开，至少要选类型')
            this.loading = false
            return
          } else {
            sxType = util.dataForDouhao(this.sx_type)
          }
        }
        let sxSc = util.dataForKongGe(this.sx_sc)
        let params = {
          type: sxType,
          numbers: number.replace(/ /g, ','),
          sc: sxSc,
          dd: util.dataForKongGe(this.sx_dd),
          dxb: util.dataForDouhao(this.sx_dxb),
          qob: util.dataForDouhao(this.sx_qob)
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
          this.zhuNum = index
          this.value_numbers = content

          this.sxBtnDisable = true
          this.sxSwitch = false
          this.sx_type = []
          this.sx_sc = []
          this.sx_dd = []
          this.sx_dxb = []
          this.sx_qob = []
          this.value_number_select_disabled = false
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
          let period = listData[i].data_period
          let award = listData[i].data_award
          let size = listData[i].data_size
          let qiou = listData[i].data_qiou
          let zhihe = listData[i].data_zhihe
          if (type === 'M1') {
            data.push({
              data_period: period,
              data_award: award,
              data_type: type,
              data_size: size,
              data_qiou: qiou,
              data_zhihe: zhihe,
              cellClassName: {
                data_type: 'table-info-cell-type1'
              }
            })
          } else if (type === 'M2') {
            data.push({
              data_period: period,
              data_award: award,
              data_type: type,
              data_size: size,
              data_qiou: qiou,
              data_zhihe: zhihe,
              cellClassName: {
                data_type: 'table-info-cell-type2'
              }
            })
          } else if (type === 'M3') {
            data.push({
              data_period: period,
              data_award: award,
              data_type: type,
              data_size: size,
              data_qiou: qiou,
              data_zhihe: zhihe,
              cellClassName: {
                data_type: 'table-info-cell-type3'
              }
            })
          } else if (type === 'M4') {
            data.push({
              data_period: period,
              data_award: award,
              data_type: type,
              data_size: size,
              data_qiou: qiou,
              data_zhihe: zhihe,
              cellClassName: {
                data_type: 'table-info-cell-type4'
              }
            })
          } else {
            data.push({
              data_period: period,
              data_award: award,
              data_type: type,
              data_size: size,
              data_qiou: qiou,
              data_zhihe: zhihe
            })
          }
        }
        this.tableData = data
        this.tableLoading = false
      }
    },
    doCopy () {
      this.$copyText(this.value_numbers).then(function (e) {
        util.messgeSuccess('组选号码已经复制到剪贴板')
      }, function (e) {
        util.messgeError('复制失败')
      })
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
  input:focus, textarea:focus {
      outline: none;
  }
  textarea {
    resize: none;
  }
  .card-title {
    color: #abafbd;
    font-size: 20px;
  }
  .ivu-table .table-info-cell-type1 {
    color: rgb(3, 160, 250);
    font-weight: bold;
  }
  .ivu-table .table-info-cell-type2 {
    color: rgb(243, 18, 18);
    font-weight: bold;
  }
  .ivu-table .table-info-cell-type3 {
    color: rgb(50, 167, 35);
    font-weight: bold;
  }
  .ivu-table .table-info-cell-type4 {
    color: rgb(210, 17, 228);
    font-weight: bold;
  }
</style>
