<template>
    <div class="login">
    <div class="login-con">
      <Card title="欢迎登录" :bordered="false">
        <div class="form-con">
          <login-form @on-success-valid="handleSubmit"></login-form>
        </div>
      </Card>
    </div>
  </div>
</template>
<script>
import LoginForm from './components/login-form'
export default {
  components: {
    LoginForm
  },
  methods: {
    handleSubmit ({ userName, password }) {

    }
  }
}
</script>

<style scoped>

</style>
