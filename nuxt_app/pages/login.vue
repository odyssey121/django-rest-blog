<template>
  <div class="q-pa-md login-form">
    <div>
      <q-btn-toggle
        v-model="isLogin"
        toggle-color="primary"
        push
        glossy
        :options="[
          { label: 'Login', value: true },
          { label: 'Register', value: false }
        ]"
      />
    </div>
    <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
      <q-input
        filled
        v-model="email"
        label="Your email *"
        hint="your email address"
        lazy-rules
        :rules="[
          val => (val && val.length > 0) || 'Please enter email',
          val => /\S+@\S+\.\S+/.test(val) || 'Email address is wrong!'
        ]"
      >
        <template v-slot:append> <q-icon name="email" /> </template
      ></q-input>

      <q-input
        v-model="password"
        filled
        :type="isPwd ? 'password' : 'text'"
        hint="Password"
        :rules="[
          val => !!val || '* Required',
          val => val.length > 4 || 'Please use maximum 4 character'
        ]"
      >
        <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
      </q-input>

      <div class="q-pa-md btn-bottom">
        <q-btn type="submit" color="primary" style="width:224px;">{{
          isLogin ? "Login" : "Registration"
        }}</q-btn>
        <q-btn
          label="Reset"
          type="reset"
          color="primary"
          flat
          class="q-ml-sm"
        />
      </div>
    </q-form>
  </div>
</template>

<script>
export default {
  computed: {},
  data() {
    return {
      isPwd: true,
      isLogin: true,
      email: "",
      password: ""
    };
  },
  methods: {
    onSubmit(e) {
      console.log(e);
    },
    onReset() {
      console.log("onReset");
    }
  }
};
</script>

<style scoped>
.auth-container {
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 2px #ccc;
  width: 300px;
  margin: auto;
  padding: 10px;
  box-sizing: border-box;
}
.login-form {
  margin: auto;
  margin-top: 10%;
  max-width: 400px;
}
.btn-bottom {
  display: flex;
  justify-content: space-between;
}
.login-form > div {
  width: 100;
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}
</style>
