<template>
    <div class="cart-page">
        <div class="uk-card uk-card-small uk-card-default uk-card-body">
            <div class="uk-padding">
                <el-steps :active="active" finish-status="success" align-center>
                    <el-step title="Корзина"></el-step>
                    <el-step title="Доставка"></el-step>
                    <el-step title="Готово"></el-step>
                </el-steps>
            </div>
            <div class="cart" v-if="active === 0">
                <el-table
                        :data="items"
                        border
                        style="width: 100%"
                        size="mini"
                        fit
                        show-header
                >
                    <el-table-column
                            type="index"
                            label="#"
                            width="50">
                    </el-table-column>
                    <el-table-column
                            width="100"
                            align="center"
                    >
                        <template slot-scope="scope">
                            <img class="uk-preserve-width uk-border-rounded" :src="scope.row.image" width="70"
                                 alt=""
                                 v-if="scope.row.image">
                            <img class="uk-preserve-width uk-border-rounded"
                                 src="/static/src/assets/img/noimage.png"
                                 width="70"
                                 alt="" v-else>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="name"
                            label="Наименование">
                    </el-table-column>
                    <el-table-column
                            prop="price"
                            label="Цена"
                            width="80"
                            align="center"
                            suffix="р."
                    >
                    </el-table-column>
                    <el-table-column
                            label="Кол-во"
                            width="150"
                            align="center"
                    >
                        <template slot-scope="scope">
                            <el-input-number v-model="scope.row.qty" @change="handleChangeQty(scope.row)" :min="1"
                                             :max="20" size="mini"></el-input-number>
                        </template>
                    </el-table-column>
                    <el-table-column
                            label="Сумма"
                            width="80"
                            align="center"
                    >
                        <template slot-scope="scope">
                            {{scope.row.price * scope.row.qty}} р.
                        </template>
                    </el-table-column>
                </el-table>
                <div class="uk-flex uk-padding uk-flex-between">
                    <div>
                        <el-button type="success" @click="next">Оформить заказ</el-button>
                    </div>
                    <div>
                        <span class="uk-text-large">Итого: {{total}}  руб.</span>
                    </div>
                </div>
            </div>
            <div class="delivery" v-else-if="active === 1">
                <el-form :inline="true" :model="formDelivery">
                    <el-form-item label="Ваше Имя">
                        <el-input v-model="formDelivery.name" placeholder="Ваше Имя">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Номер телефона">
                        <el-input v-model="formDelivery.name" placeholder="+7 999 999-99-99">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Ваше Имя">
                        <el-input v-model="formDelivery.name" placeholder="Ваше Имя">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Ваше Имя">
                        <el-input v-model="formDelivery.name" placeholder="Ваше Имя">
                        </el-input>
                    </el-form-item>
                    <el-form-item label="Ваше Имя">
                        <el-input v-model="formDelivery.name" placeholder="Ваше Имя">
                        </el-input>
                    </el-form-item>
                </el-form>
            </div>
            <div class="success" v-else-if="active === 2">

            </div>
        </div>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'

    export default {
        name: "cart-page",
        data: () => ({
            active: 0,
            formDelivery: {
                name: null,
                phone: null,
                address: null,
                area: null,
                person: 1,
            }
        }),
        created () {
            this.getCart()
        },
        computed: {
            ...mapGetters({
                items: 'getItems',
                total: 'getTotal'
            })
        },
        methods: {
            ...mapActions({
                getCart: 'getCartItems',
                changeItemCart: 'changeItemCart'
            }),
            handleChangeQty (item) {
                this.changeItemCart(item)
            },
            next () {
                this.active++
            }
        }
    }
</script>

<style scoped>

</style>