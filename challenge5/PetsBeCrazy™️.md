# PetsBeCrazy™️ API Documentation

## Endpoints

Base URL:

```bash
http://www.petsbecrazy.com
```

### As a shopper, I can go to the homepage of the store

```bash
GET /shop
```

### As a shopper, I can go to a page showing the store’s recommended dog foods

```bash
GET /shop/foods/dog
```

### As a shopper, I can go to a page showing the dog foods that are on sale

```bash
GET /shop/foods/dog?discount=true
```

### As a shopper, I can go to a page showing only _Hills_ brand dog foods

```bash
GET /shop/foods/dog?brand=Hills
```

### As a shopper, I can go to a page showing all dog foods except for _Montego_ brand dog foods

```bash
GET /shop/foods/dog?excludeBrand=Montego
```

### As a shopper, I can go to a page showing all cat foods

```bash
GET /shop/foods/cat
```

### As a shopper, I can search for products containing the text “puppy”

```bash
GET /shop/products?query=puppy
```

### As a shopper, I can search for dog foods containing the text “puppy”

```bash
GET /shop/foods/dog?query=puppy
```

### As an admin, I can go to a dashboard page where I can edit all the site’s products

```bash
GET /admin
Header:
{
  "API_KEY": "<SUPER_SECRET_ADMIN_API_KEY>"
}
```

-> Header is present in all admin endpoints.

### As an admin, I can go to a page where I can add a new dog food (what is the URL of the page I am on when I am typing in the new dog food details?)

```bash
GET /admin/create
```

-> Generic page to create any product, with form to specify details needed. See next endpoint for details.

### As an admin, I can save a new dog food (what is the verb + route of the request that’s triggered when I click “Save”?)

```bash
POST /admin/create
Body:
{
  "category": "food",
  "animal": "dog",
  "brand": "Ultra Dog",
  "name": "OptiWoof Adult",
  ...
}
```
