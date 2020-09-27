<template lang="html">
  <div class="mt-3">
    <div v-if="notFound" class="container">
      <h4>Oups, we cannot find the question you're searching for</h4>
    </div>
    <div v-else class="container">
      <div id="questionHeader">
        <div id="questionTitle" class="mr-5">
          <h5>{{question.content | questionize}}</h5>
        </div>
        <div id="questionActions" class="ml-5">
          <QuestionActions v-if="isAuthor" :slug="slug"/>
        </div>
      </div>
      <p class="mt-3 mb-0">
        Question asked by
        <span class="author">{{question.author | capitalize}}</span>
      </p>
      <p>{{question.creationDate}}</p>
      <hr>
      <template v-if="hasAnswered">
        <p class="answered">You've already answered this question</p>
      </template>
      <template v-else-if="!showForm">
        <button class="btn" @click="showForm=true">Answer this question</button>
      </template>
      <template v-else>
        <form @submit.prevent="onSubmit">
          <textarea v-model="newAnswer" class="form-control"
            placeholder="Type your answer here" rows="5"></textarea>
          <button class="btn mt-2" type="submit">Add answer</button>
        </form>
        <p class="error mt-2">{{error}}</p>
      </template>
      <hr>
      <AnswerComponent v-for="(answer, index) in answers" :answer="answer"
        :userName="userName" :key="index" @deleteAnswer="deleteAnswer"/>
      <div class="my-4">
        <p v-show="loadingAnswers">loading more answers...</p>
        <button v-show="next" @click="getQuestionAnswers" class="btn">
          Lode more answers
        </button>
      </div>
    </div>
  </div>
</template>

<script>
  import {APIService} from "../common/API.service";
  import AnswerComponent from "../components/Answer.vue";
  import QuestionActions from "../components/QuestionActions.vue";
  export default {
    name: "Question",
    props: {
      slug: {
        type: String,
        required: true
      }
    }, components: {AnswerComponent, QuestionActions},
    data() {return {
      question: {},
      loadingAnswers: false,
      answers: [],
      hasAnswered: false,
      showForm: false,
      newAnswer: null,
      error: null,
      next: null,
      userName: null
    }}, computed: {
      isAuthor() {return this.question.author === this.userName;},
      notFound() {return this.question.detail}
    }, methods: {
      setPageTitle(ID) {document.title = "Question " + ID + " - Questio";},
      getUserName() {this.userName = window.localStorage.getItem("userName");},
      getQuestionData() {
        let endpoint = `/API/questions/${this.slug}/`;
        APIService(endpoint)
          .then(data => {
            this.question = data;
            this.hasAnswered = data.hasAnswered;
            this.setPageTitle(data.id);
          })
      }, getQuestionAnswers() {
        let endpoint = `/API/question/${this.slug}/answers/`;
        if (this.next) {endpoint = this.next;}
        this.loadingAnswers = true;
        APIService(endpoint)
          .then(data => {
            this.answers.push(...data.results);
            this.loadingAnswers = false;
            if (data.next) {this.next = data.next;}
            else {this.next = null;}
          })
      }, onSubmit() {
        if (this.newAnswer) {
          let endpoint = `/API/question/${this.slug}/answer/`;
          APIService(endpoint, "POST", {content: this.newAnswer})
            .then(data => {this.answers.unshift(data);})
          this.newAnswer = null;
          this.showForm = false;
          this.hasAnswered = true;
          if (this.error) {this.error = null;}
        }
        else {this.error = "Answer text cannot be empty"}
      }, async deleteAnswer(answer) {
        let endpoint = `/API/answers/${answer.id}`;
        try {
          await APIService(endpoint, "DELETE");
          this.answers.splice(this.answers.indexOf(answer), 1);
          this.hasAnswered = false;
        } catch(err) {console.log(err);}
      }
    }, created() {
      this.getQuestionData();
      this.getQuestionAnswers();
      this.getUserName();
    }
  }
</script>

<style lang="css" scoped>
  #questionHeader {display: inline-table}
  #questionTitle {display: inline-block;
                  vertical-align: middle}
  #questionActions {display: inline-block}
  h5 {font-weight: bold;
      margin: 0;
      padding: 0}
  .answered {color: var(--colour3);
             font-weight: bold}
</style>
