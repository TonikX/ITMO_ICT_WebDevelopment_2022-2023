<template>
    <v-toolbar app flat>
        <v-app-bar-nav-icon
                class="d-flex d-md-none"
                variant="text"
                @click="drawer=true">
        </v-app-bar-nav-icon>

        <v-toolbar-title style="flex: 0 0 auto">
            <v-icon icon="mdi-circle-slice-4"/>
            Admin Cosmo
        </v-toolbar-title>

        <div class="d-none d-md-flex">
            <v-btn
                    v-for="link in links"
                    :key="link.name"
                    :to="link"
                    class="ms-3"
                    variant="text"
            >
                {{ link.label }}
            </v-btn>
        </div>
    </v-toolbar>

    <v-navigation-drawer
            v-model="drawer"
            absolute
            temporary>
        <v-list
                nav
        >
            <v-list-item v-for="link in links">
                <v-btn
                        :key="link.name"
                        :to="link"
                        variant="text"
                >
                    {{ link.label }}
                </v-btn>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
	name: "UnauthenticatedMenuComponent",
	data: () => ({
		drawer: false,
		links: [
			{name: "SignIn", label: "Войти"},
			{name: "SignUp", label: "Зарегистрироваться"},
		]
	})
}
</script>
