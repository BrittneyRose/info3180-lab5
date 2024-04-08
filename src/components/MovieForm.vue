<template>
    <form @submit.prevent="saveMovie" enctype="multipart/form-data" id="movieForm">
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="form-control" />
        </div>

        <div class="form-group mb-3">
            <label for="poster" class="form-label">Upload Poster</label>
            <input type="file" name="poster" accept="image/*" class="form-control-file" />
        </div>

        <div class="form-group mb-3">
            <label for="description" class="form-label">Description</label>
            <input type="text" name="description" class="form-control" />
        </div>
        
        <button type="submit" >Submit</button>
    </form>

</template>

<script setup>

import { ref, onMounted } from "vue";
let csrf_token = ref("");

onMounted(() => {
    // getCsrfToken();
    csrf_token.value = '237';
});

// function getCsrfToken() {
//     fetch('/api/v1/csrf-token')
//       .then((response) => response.json())
//       .then((data) => {
//         console.log(data);
//         csrf_token.value = data.csrf_token;
//       })
// }


function saveMovie()  {
    let movieForm =document.getElementById('movieForm');
    let form_data = new FormData(movieForm);
    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        console.log(data);
    })
    .catch(function (error) {
        console.log(error);
    });
}


</script>

