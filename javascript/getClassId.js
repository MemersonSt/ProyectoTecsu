const classId = getClassByIdFromNameFile();

export function getClassByIdFromNameFile() {
    const nameFile = window.location.pathname.split("/").pop();
    const numberClass = nameFile.replace("FormClase", "").replace(".html", "");
    return parseInt(numberClass);
}
