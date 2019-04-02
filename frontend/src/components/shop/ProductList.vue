<template>
    <div class="uk-flex-left uk-margin-auto-vertical uk-child-width-1-5@m" uk-grid>
        <div v-for="product in products" :key="product.id">
            <div class="uk-card uk-card-small uk-card-default">
                <div class="uk-card-media-top">
                    <img :src="product.image" alt="">
                </div>
                <div class="uk-card-body uk-text-center">
                    {{product.name}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "product-list",
        props: {
            limit: {
                type: Number,
                default: 30
            },
            category: {
                type: Number,
                required: true
            }
        },
        data: () => ({
            products: [],
            count: 0,
            next: null,
            previous: null,
        }),
        created () {
            this.getProducts()
        },
        methods: {
            async getProducts () {
                let {data} = await this.$axios.get(`/api/products?category=${this.category}&page_size=${this.limit}`)
                this.products = data.results
                this.count = data.count
                this.next = data.next
                this.previous = data.previous
            }
        }
    }
</script>

<style scoped>

</style>