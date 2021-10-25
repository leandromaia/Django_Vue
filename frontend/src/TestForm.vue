<template>
    <div id="app" class="ml-5">
        <div class="card text-left">
            <div class="card-body">
                <h5 class="card-title">Cadastro de Pessoa</h5>
                <form>
                    <div class="form-group">
                        <label for="exampleFormControlInput1">Nome:</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1"
                            v-model="form.first_name">
                    </div>

                    <div class="form-group">
                        <label for="exampleFormControlInput1">Sobrenome:</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1"
                            v-model="form.last_name">
                    </div>

                    <div class="form-group">
                        <label for="exampleFormControlInput1">Email address</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1"
                               placeholder="name@example.com" v-model="form.email">
                    </div>                  
                </form>
                <button v-on:click="submit()">Submit</button>
            </div>
        </div>
    </div>
</template>


<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

<script>
const axios = require('axios');
export default {
    data(){
        return {
            form: {
                first_name: '',
                last_name: '',
                email: ''
            }
        }
    },

    methods: {
        submit(){
            axios.post('http://127.0.0.1:8000/api/person/', this.form)
                .then(function( response ){
                    this.form.first_name = null;
                    this.form.last_name = null;
                    this.form.email = null;
                    alert('Cadastro realizado com sucesso!');
                }.bind(this));
        }
    }
}
</script>

<style scoped>
    .card {
        max-width: 500px;
    }

</style>