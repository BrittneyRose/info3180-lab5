import { createApp } from 'vue'; 
import App from './App.vue';
import router from './router';
import MovieForm from './components/MovieForm.vue'; 

const app = createApp(App);

app.use(router);

// Register MovieForm as a global component
app.component('MovieForm', MovieForm);

app.mount('#app');
