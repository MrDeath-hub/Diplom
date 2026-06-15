// БОЛЬШОЙ МАССИВ ВСЕХ ВОПРОСОВ (можно легко добавлять новые)
const allQuestions = [
    {
        question: "Кто был первым человеком, вышедшим в открытый космос?",
        options: ["Нил Армстронг", "Алексей Леонов", "Джон Гленн", "Валентина Терешкова"],
        correct: 1
    },
    {
        question: "Как называлась ракета, на которой Юрий Гагарин совершил первый полёт?",
        options: ["Союз", "Восток", "Протон", "Энергия"],
        correct: 1
    },
    {
        question: "Какая планета Солнечной системы самая большая?",
        options: ["Сатурн", "Нептун", "Юпитер", "Уран"],
        correct: 2
    },
    {
        question: "Сколько минут длился первый полёт Юрия Гагарина?",
        options: ["108 минут", "90 минут", "120 минут", "60 минут"],
        correct: 0
    },
    {
        question: "Как называется ближайшая к Земле звезда (кроме Солнца)?",
        options: ["Сириус", "Проксима Центавра", "Альфа Центавра", "Бетельгейзе"],
        correct: 1
    },
    {
        question: "Кто был первой женщиной-космонавтом?",
        options: ["Светлана Савицкая", "Елена Кондакова", "Валентина Терешкова", "Пегги Уитсон"],
        correct: 2
    },
    {
        question: "Какое небесное тело было лишено статуса планеты в 2006 году?",
        options: ["Плутон", "Эрида", "Церера", "Макемаке"],
        correct: 0
    },
    {
        question: "Как называется галактика, в которой мы живём?",
        options: ["Туманность Андромеды", "Млечный Путь", "Водоворот", "Треугольник"],
        correct: 1
    },
    {
        question: "Какой космический аппарат первым достиг поверхности Луны?",
        options: ["Аполлон-11", "Луна-2", "Луна-9", "Сервейер-1"],
        correct: 1
    },
    {
        question: "Кто из этих космонавтов совершил самый длительный одиночный полёт (437 суток)?",
        options: ["Сергей Крикалёв", "Валерий Поляков", "Геннадий Падалка", "Юрий Романенко"],
        correct: 1
    },
    {
        question: "Как называется самая высокая гора на Марсе?",
        options: ["Эверест", "Олимп", "Эльбрус", "Монблан"],
        correct: 1
    },
    {
        question: "Сколько спутников у Марса?",
        options: ["1", "2", "3", "4"],
        correct: 1
    },
    {
        question: "Какая планета вращается «лёжа на боку» (наклон оси около 98 градусов)?",
        options: ["Уран", "Нептун", "Сатурн", "Юпитер"],
        correct: 0
    },
    {
        question: "Как называется явление, когда Луна закрывает Солнце?",
        options: ["Затмение", "Солнечное затмение", "Лунное затмение", "Прохождение"],
        correct: 1
    },
    {
        question: "Какой космический телескоп был запущен в 1990 году и работает до сих пор?",
        options: ["Хаббл", "Джеймс Уэбб", "Спитцер", "Чандра"],
        correct: 0
    },
    {
        question: "Кто из этих учёных впервые предложил гелиоцентрическую систему мира?",
        options: ["Птолемей", "Коперник", "Галилей", "Кеплер"],
        correct: 1
    },
    {
        question: "Как называется траектория движения космического аппарата под действием силы тяжести небесного тела?",
        options: ["Орбита", "Траектория", "Линза", "Эллипс"],
        correct: 0
    },
    {
        question: "Сколько звёзд в Солнечной системе?",
        options: ["Одна", "Две", "Три", "Много"],
        correct: 0
    },
    {
        question: "Какой космонавт совершил первый выход в открытый космос 18 марта 1965 года?",
        options: ["Юрий Гагарин", "Алексей Леонов", "Павел Беляев", "Владимир Комаров"],
        correct: 1
    },
    {
        question: "Какой элемент преобладает в составе Солнца?",
        options: ["Гелий", "Кислород", "Водород", "Углерод"],
        correct: 2
    },
    {
        question: "Как называется явление «падающих звёзд»?",
        options: ["Метеоритный дождь", "Метеорный поток", "Астероидная бомбардировка", "Звёздопад"],
        correct: 1
    },
    {
        question: "Как называется первая в мире орбитальная станция?",
        options: ["Мир", "Салют-1", "Скайлэб", "Тяньгун-1"],
        correct: 1
    },
    {
        question: "Какой американский астронавт первым ступил на Луну?",
        options: ["Базз Олдрин", "Нил Армстронг", "Майкл Коллинз", "Алан Шепард"],
        correct: 1
    },
    {
        question: "Как называется самая маленькая планета Солнечной системы (после лишения статуса Плутона)?",
        options: ["Меркурий", "Марс", "Венера", "Земля"],
        correct: 0
    },
    {
        question: "Какая планета имеет самую высокую температуру поверхности?",
        options: ["Меркурий", "Венера", "Земля", "Марс"],
        correct: 1
    }
];

const QUESTIONS_PER_QUIZ = 10;

let quizQuestions = [];
let currentQuestionIndex = 0;
let userAnswers = [];
let score = 0;

function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

function selectRandomQuestions() {
    const shuffledAll = shuffleArray([...allQuestions]);
    return shuffledAll.slice(0, QUESTIONS_PER_QUIZ);
}

function showQuestion() {
    const q = quizQuestions[currentQuestionIndex];
    document.getElementById("question-text").innerText = q.question;
    const optionsContainer = document.getElementById("options-container");
    optionsContainer.innerHTML = "";
    q.options.forEach((opt, idx) => {
        const radio = document.createElement("input");
        radio.type = "radio";
        radio.name = "option";
        radio.value = idx;
        radio.id = `opt_${idx}`;
        if (userAnswers[currentQuestionIndex] === idx) radio.checked = true;
        
        const label = document.createElement("label");
        label.htmlFor = `opt_${idx}`;
        label.innerText = opt;
        
        const div = document.createElement("div");
        div.appendChild(radio);
        div.appendChild(label);
        optionsContainer.appendChild(div);
    });
    document.getElementById("question-counter").innerText = `${currentQuestionIndex+1} / ${quizQuestions.length}`;
    document.getElementById("next-btn").style.display = "inline-block";
    document.getElementById("prev-btn").style.display = currentQuestionIndex === 0 ? "none" : "inline-block";
    document.getElementById("result-container").innerHTML = "";
}

function saveCurrentAnswer() {
    const selected = document.querySelector('input[name="option"]:checked');
    if (selected) {
        userAnswers[currentQuestionIndex] = parseInt(selected.value);
    }
}

function nextQuestion() {
    saveCurrentAnswer();
    if (currentQuestionIndex < quizQuestions.length - 1) {
        currentQuestionIndex++;
        showQuestion();
    } else {
        finishQuiz();
    }
}

function prevQuestion() {
    saveCurrentAnswer();
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        showQuestion();
    }
}

function finishQuiz() {
    saveCurrentAnswer();
    let correctCount = 0;
    for (let i = 0; i < quizQuestions.length; i++) {
        if (userAnswers[i] === quizQuestions[i].correct) correctCount++;
    }
    const resultDiv = document.getElementById("result-container");
    resultDiv.innerHTML = `<div class="alert alert-info mt-3">Вы ответили правильно на ${correctCount} из ${quizQuestions.length} вопросов.</div>`;
    document.getElementById("next-btn").style.display = "none";
    document.getElementById("prev-btn").style.display = "none";
    
    const restartBtn = document.createElement("button");
    restartBtn.innerText = "🔄 Пройти викторину заново (новые вопросы)";
    restartBtn.className = "btn btn-primary mt-3";
    restartBtn.onclick = () => {
        initQuiz();
    };
    resultDiv.appendChild(restartBtn);
}

function initQuiz() {
    quizQuestions = selectRandomQuestions();
    currentQuestionIndex = 0;
    userAnswers = new Array(quizQuestions.length).fill(null);
    showQuestion();
}

document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("quiz-container");
    if (!container) return;
    container.innerHTML = `
        <div class="glass-panel p-4">
            <h2 class="gradient-text text-center"> Космическая викторина</h2>
            <p class="text-center">Проверьте свои знания о космосе! Каждый раз вопросы выбираются случайно.</p>
            <div id="question-counter" class="text-center mb-2"></div>
            <div id="question-text" class="h5 mb-3"></div>
            <div id="options-container" class="mb-3"></div>
            <div class="d-flex justify-content-between">
                <button id="prev-btn" class="btn btn-secondary">← Назад</button>
                <button id="next-btn" class="btn btn-primary">Далее →</button>
            </div>
            <div id="result-container" class="mt-3"></div>
        </div>
    `;
    initQuiz();
    document.getElementById("next-btn").addEventListener("click", nextQuestion);
    document.getElementById("prev-btn").addEventListener("click", prevQuestion);
});