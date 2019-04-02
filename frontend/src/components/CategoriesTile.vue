<template>
    <div class="categories-tile">
        <el-row class="uk-flex-wrap" :gutter="10" type="flex" justify="center" align="middle">
            <el-col :md="6" :sm="8" :xs="12" v-for="category in categories" :key="category.id">
                <section style="min-height: 140px">
                    <a :href="category.link" class="uk-text-uppercase">{{category.name}}</a>
                </section>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "CategoriesTile",
        data: () => ({
            categories: []
        }),
        mounted () {
            this.getCategories()
        },
        methods: {
            async getCategories () {
                let {data} = await this.$axios.get('/api/categories')
                this.categories = data
            }
        }
    }
</script>

<style scoped>

</style>