import AnswerEditor from "../views/AnswerEditor.vue";
import Home from "../views/Home.vue";
import NotFound from "../views/NotFound.vue";
import Question from "../views/Question.vue";
import QuestionEditor from "../views/QuestionEditor.vue";
import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/answer/:id",
    name: "AnswerEditor",
    component: AnswerEditor,
    props: true
  }, {
    path: "/",
    name: "Home",
    component: Home
  }, {
    path: "*",
    name: "PageNotFound",
    component: NotFound
  }, {
    path: "/question/:slug",
    name: "Question",
    component: Question,
    props: true
  }, {
    path: "/ask/:slug?",
    name: "QuestionEditor",
    component: QuestionEditor,
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
