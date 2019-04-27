<template>
    <div class="cart-items">
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
                    <img class="uk-preserve-width uk-border-rounded" :src="scope.row.image" width="70" alt=""
                         v-if="scope.row.image">
                    <img class="uk-preserve-width uk-border-rounded" src="/static/src/assets/img/noimage.png" width="70"
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
    </div>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'

    export default {
        name: "cart-items",
        created() {
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
            handleChangeQty(item) {
                this.changeItemCart(item)
            }
        }
    }
</script>

<style scoped>

</style>