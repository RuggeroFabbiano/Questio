<template lang="html">
  <div class="container mt-3">
    <h4 class="mb-3">Edit answer</h4>
    <form @submit.prevent="onSubmit">
      <textarea v-model="answerContent" class="form-control" rows="3">
      </textarea>
      <br>
      <button class="btn" type="submit">Post answer</button>
    </form>
    <p class="error mt-3">{{error}}</p>
  </div>
</template>

<script>
  import {APIService} from "../common/API.service.js";
  export default {
    name: "AnswerEditor",
    props: {
      id: {
        type: Number,
        required: true
      }
    }, data() {return{
      answerContent: null,
      questionSlug: null,
      error: null
    }}, methods: {
      setPageTitle(ID) {document.title = "Answer " + ID + " - Questio";},
      async getAnswerData() {
        let endpoint = `/API/answers/${this.id}`;
        await APIService(endpoint)
          .then(data => {
            this.answerContent = data.content;
            this.questionSlug = data.questionSlug;
            this.setPageTitle(data.id);
          })
      }, onSubmit() {
        if (this.answerContent) {
          let endpoint = `/API/answers/${this.id}`;
          APIService(endpoint, "PUT", {content: this.answerContent})
            .then(() => {
              this.$router.push({
                name: "Question",
                params: {slug: this.questionSlug}
              })
            })
        } else {this.error = "Answer field cannot be empty";}
      }
    }, created() {this.getAnswerData();}
  }
</script>
