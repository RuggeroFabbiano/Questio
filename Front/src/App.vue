<template>
  <div id="app">
    <NavBarComponent/>
    <router-view/>
  </div>
</template>

<script>
  import NavBarComponent from "./components/NavBar.vue";
  import {APIService} from "./common/API.service";
  export default {
    name: "App",
    components: {NavBarComponent},
    data() {return{userName: "null"}},
    methods: {
      async setUserName() {
        await APIService("/API/user")
          .then(result => {
            this.userName = result.username;
            window.localStorage.setItem("userName", this.userName);
          })
      }
    }, created() {this.setUserName()}
  }
</script>
