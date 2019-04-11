<template>
    <div class="uk-card uk-card-small uk-card-default pub-product-card">
        <div class="uk-card-media-top uk-cover-container uk-height-medium">
            <img :src="product.image" class="uk-align-center" :alt="product.name" uk-cover>
        </div>
        <div class="uk-card-body uk-text-center uk-padding-remove">
            <span class="pub-product-name">{{product.name}}</span>
            <br>
            <small class="uk-text-muted">{{product.quantity}} шт.</small>
            <div class="uk-flex uk-grid-small uk-child-width-1-2 uk-flex-middle uk-grid-match uk-margin-auto-vertical"
                 uk-grid>
                <div class="uk-text-muted uk-text-center">
                    <span>{{product.weight}} гр.</span>
                </div>
                <div class="pub-product-price uk-text-center">
                    <span>{{product.price}} ₽</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "product-card",
        props: ['product']
    }
</script>

<style scoped>

</style>