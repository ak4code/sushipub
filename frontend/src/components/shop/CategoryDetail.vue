<template>
    <div class="pub-category-detail">
        <div class="uk-flex uk-grid-small uk-grid-match uk-margin-small-bottom uk-child-width-1-1 uk-child-width-1-5@m"
             uk-grid v-if="products">
            <div v-for="product in products.results" :key="product.id">
                <product-card :product="product"></product-card>
            </div>
        </div>
    </div>
</template>

<script>
    import ProductCard from '@/components/shop/ProductCard'

    export default {
        name: "category-detail",
        props: {
            categoryId: {
                type: Number,
                required: true
            }
        },
        data: () => ({
            category: null,
            products: null,
        }),
        components: {
            ProductCard
        },
        created () {
            this.getProducts()
        },
        methods: {
            async getProducts () {
                let {data} = await this.$axios.get(`/api/products?category=${this.categoryId}`)
                this.products = data
                await this.getCategory()
            },
            async getCategory () {
                let {data} = await this.$axios.get(`/api/categories/${this.categoryId}`)
                this.category = data
            }
        }
    }
</script>

<style scoped>

</style>