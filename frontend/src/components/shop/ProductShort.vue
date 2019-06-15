<template>
    <div v-loading="loading">
        <div class="uk-flex uk-grid-small uk-grid-match uk-margin-bottom uk-child-width-1-1 uk-child-width-1-3@s uk-child-width-1-4@m uk-child-width-1-5@l"
             uk-grid v-if="products.length">
            <div v-for="product in products" :key="product.id">
                <product-card :product="product"></product-card>
            </div>
        </div>
    </div>
</template>

<script>
    import ProductCard from '@/components/shop/ProductCard'

    export default {
        name: "product-list",
        props: {
            productId: {
                type: Number,
                required: true
            }
        },
        components: {
            ProductCard,

        },
        data: () => ({
            products: [],
            loading: true
        }),
        created () {
            this.getProducts()
        },
        methods: {
            async getProducts () {
                let {data} = await this.$axios.get(`/api/products/short_list?product=${this.productId}`)
                this.products = data
                this.loading = false
            }
        }
    }
</script>

<style scoped>

</style>