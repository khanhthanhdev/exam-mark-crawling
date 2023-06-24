import fs from "fs";
const students = JSON.parse(fs.readFileSync("../data/data.json"));

const parseField = (str, field) =>
  Number(str.split(field)[1]?.split(";")[0].trim());

const parsed = students
  .map((student) => ({
    ...student,
    total: parseField(student.mark, "Total:"),
    literature: parseField(student.mark, "Liter:"),
    math: parseField(student.mark, "Math:"),
    english: parseField(student.mark, "Lang:"),
    professional1: parseField(student.mark, "Ex 1:"),
    professional2: parseField(student.mark, "Ex 2:"),
  }))
  .filter((i) => i.total);

console.log("Tổng số học sinh", students.length);

console.log(
  "Số người thi chuyên",
  parsed.filter((i) => i.professional1 || i.professional2).length
);

console.log(
  "Số người có điểm trên 47: ",
  parsed.filter((i) => i.total >= 47.00).length
)
console.log(
  "Số người điểm văn >= 9",
  parsed.filter((i) => i.literature >= 9.00).length
);
console.log(
  "Số người điểm văn = 9.5",
  parsed.filter((i) => i.literature === 9.50).length
);

console.log(
  "Số người điểm văn >= 8",
  parsed.filter((i) => i.literature >= 8.00).length
);

console.log(
  "Số người điểm toán = 10",
  parsed.filter((i) => i.math === 10.00).length
);

console.log(
  "Số người điểm tiếng anh = 10",
  parsed.filter((i) => i.english === 10.00).length
);

console.log(
  "Số người điểm chuyên 1 = 10",
  parsed.filter((i) => i.professional1 === 10.00).length
);

console.log(
  "Số người điểm chuyên 2 = 10",
  parsed.filter((i) => i.professional2 === 10.00).length
);
