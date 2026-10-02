function Hello_Button(){
alert("Hello ;)")
}

function Update_Name(){
    let Name=document.getElementById("Name").value;

    document.getElementById("Name_Holder").innerHTML=Name;
    us
}

function calc_mean (){
//get user data
let data_from_user = document.getElementById('dataset1').value;
//split string data_from_user to list
let data_list = data_from_user.split(',')
//set up variables
let total = 0
let num_items = 0
//iterate through the list to get total
for (let temp of data_list){
//input is text so we need to cast to float
    total = total + parseFloat(temp);
}
//get num of items in list
num_items = data_list.length;
//calculate mean
let mean = total / num_items;

return mean;

}

function calc_median(){
    //get user data
    let data_from_user = document.getElementById('dataset1').value;
    //split string data_from_user to list
    let data_list = data_from_user.split(',');
    //sort the list
    data_list.sort(function(a, b) {
        return parseFloat(a) - parseFloat(b);
    });
    //get the median
    let median;
    let num_items = data_list.length;
    if (num_items % 2 === 0) {
        //even number of items
        let mid1 = parseFloat(data_list[num_items / 2 - 1]);
        let mid2 = parseFloat(data_list[num_items / 2]);
        median = (mid1 + mid2) / 2;
    } else {
        //odd number of items
        median = parseFloat(data_list[Math.floor(num_items / 2)]);
    }
    return median;
}

function calc_mode() {
    //get user data
    let data_from_user = document.getElementById('dataset1').value;
    //split string data_from_user to list
    let data_list = data_from_user.split(',');
    //count occurrences of each number
    let counts = {};
    for (let num of data_list) {
        let parsedNum = parseFloat(num);
        counts[parsedNum] = (counts[parsedNum] || 0) + 1;
    }
    //find the maximum count
    let maxCount = Math.max(...Object.values(counts));
    //find all numbers with the maximum count
    let modes = Object.keys(counts).filter(key => counts[key] === maxCount);
    //convert back to floats
    modes = modes.map(parseFloat);
    //return the modes
    return modes;
}

function calc_range() {
    //get user data
    let data_from_user = document.getElementById('dataset1').value;
    //split string data_from_user to list
    let data_list = data_from_user.split(',');
    //convert to floats
    data_list = data_list.map(parseFloat);
    //find min and max
    let min = Math.min(...data_list);
    let max = Math.max(...data_list);
    //calculate range
    let range = max - min;
    return range;
}

function calc_btn(){
    document.getElementById('user_data_placeholder1').innerHTML=calc_mean();
    document.getElementById('user_data_placeholder2').innerHTML=calc_median();
    document.getElementById('user_data_placeholder3').innerHTML=calc_mode();
    document.getElementById('user_data_placeholder4').innerHTML=calc_range();
}

