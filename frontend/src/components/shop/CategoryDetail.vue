<template>
    <div class="pub-category-detail">
        <div v-if="products.hasOwnProperty('count') && products.count !== 0">
            <div class="uk-flex uk-grid-small uk-grid-match uk-margin-small-bottom uk-child-width-1-1 uk-child-width-1-5@m"
                 uk-grid>
                <div v-for="product in products.results" :key="product.id">
                    <product-card :product="product"></product-card>
                </div>
            </div>
            <br>
            <div class="uk-flex uk-flex-center uk-margin" v-if="products.next">
                <div>
                    <a :href="products.next" class="uk-button uk-button-default">Показать еще</a>
                </div>
            </div>
        </div>
        <div v-else>
            <div class="uk-flex uk-flex-center uk-padding-large">
                <div class="uk-text-center">
                    <h2 class="uk-text-center">Раздел еще не заполнен</h2>
                    <a href="/" class="uk-button uk-button-default">Вернуться на главную</a>
                </div>
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
            products: {},
        }),
        components: {
            ProductCard
        },
        created() {
            this.getProducts()
        },
        methods: {
            async getProducts() {
                let {data} = await this.$axios.get(`/api/products?category=${this.categoryId}`)
                this.products = data
                await this.getCategory(data.results)
            },
            async getCategory(res) {
                if (res[0].hasOwnProperty('category_info')) this.category = await res[0].category_info
            }
        }
    }
</script>

<style scoped>

</style>