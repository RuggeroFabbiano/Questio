<template lang="html">
  <div class="container mt-2">
    <div class="row">
      <div class="col-12">
        <h1 class="mb-3">Ask a new question</h1>
        <form @submit.prevent="onSubmit">
          <textarea v-model="questionBody" class="form-control"
            placeholder="Ask anything!" rows="3"></textarea>
          <br>
          <button class="btn" type="submit" >Ask it!</button>
        </form>
        <p class="error mt-2">{{error}}</p>
      </div>
    </div>
  </div>
</template>

<script>
  import {APIService} from "../common/API.service";
  export default {
    name: "QuestionEditor",
    props: {
      slug: {
        type: String,
        required: false
      }, questionContent: {
        type: String,
        required: false
      }
    },
    data() {return {
      questionBody: this.questionContent || null,
      error: null
    }}, async beforeRouteEnter(to, from, next) {
      if (to.params.slug !== undefined) {
        let endpoint = `/API/questions/${to.params.slug}/`;
        await APIService(endpoint)
        .then((data) => {to.params.questionContent = data.content;})
      } return next();
    }, methods: {
      onSubmit() {
        if (!this.questionBody)
          {this.error = "Question content cannot be empty"}
        else if (this.questionBody.length>150)
          {this.error = "Your question must not be longer than 150 characters"}
        else {
          let endpoint = "/API/questions/";
          let method = "POST";
          if (this.questionContent) {
            method = "PUT";
            endpoint += `${this.slug}/`;
          } APIService(endpoint, method, {content: this.questionBody})
            .then(questionData => {
              this.$router.push({
                name: "Question",
                params: {slug: questionData.slug}
              });
            });
        }
      }
    }, created() {document.title = "New question - Questio";}
  }
</script>
