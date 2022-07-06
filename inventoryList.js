function inventoryList() {
    // assign list
    let items = []
    
    //add a name to list.
    const add = (name) => {
        const names = items.filter(item => item.name === name)
        if (names.length === 0) {
            items.push({name: name})
        }
    }
    //remove a name from list.
    const remove = (name) => {
        items = items.filter(item => item.name !== name)
    }
    // get list of names.
    const getList = () => {
        return items
    }
    return {add, remove, getList}

}

function main() 