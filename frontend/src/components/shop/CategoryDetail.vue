<template>
    <div class="pub-category-detail">

    </div>
</template>

<script>
    export default {
        name: "category-detail",
        props: {
            categoryId: {
                type: Number,
                required: true
            }
        },
        data: () => ({
            category: null
        }),
        methods: {
            async getCategory () {
                let {data} = await this.$axios.get(`/api/categories/${this.categoryId}`)
                this.category = data
            }
        }
    }
</script>

<style scoped>

</style>