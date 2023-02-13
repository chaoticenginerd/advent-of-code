// Day 01: Calorie Counting

fn main() {
    let lines = include_str!("input.txt")
        .lines()
        .map(|line| line.parse::<u64>().ok())
        .collect::<Vec<_>>();
    let inventories = lines
        .split(|line| line.is_none())
        .map(|group| group.iter().map(|x| x.unwrap()).collect::<Vec<_>>())
        .collect::<Vec<_>>();

    println!("Part one: {}", part_one(&inventories));
    println!("Part two: {}", part_two(&inventories));
}

fn part_one(input: &Vec<Vec<u64>>) -> u64 {
    input.iter().map(|group| group.iter().sum()).max().unwrap()
}

fn part_two(input: &Vec<Vec<u64>>) -> u64 {
    let mut calorie_vec = input
        .iter()
        .map(|group| group.iter().sum())
        .collect::<Vec<u64>>();
    calorie_vec.sort();
    calorie_vec.reverse();
    calorie_vec.iter().take(3).sum()
}
